"""
Core RAG + LLM logic for SubsidySense.

Pipeline per query:
  1. Retrieve   -> filter by item category, then by state/level match, then
                   TF-IDF rank within that pool
  2. Augment    -> build a grounded prompt with the retrieved scheme snippet(s)
  3. Generate   -> Groq-hosted LLM returns a structured eligibility verdict
  4. Present    -> every answer carries the scheme's source_url and a
                   mandatory disclaimer (added in the UI layer, app.py)
"""

import json
import re
from dataclasses import dataclass, field

from groq import Groq
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils.schemes_kb import SCHEMES

MODEL_NAME = "openai/gpt-oss-120b"  # current Groq model as of Sept 2026

_KB_TEXTS = [entry["text"] for entry in SCHEMES]
_VECTORIZER = TfidfVectorizer(stop_words="english")
_KB_MATRIX = _VECTORIZER.fit_transform(_KB_TEXTS)


@dataclass
class EligibilityResult:
    item_category: str
    description: str
    price: float
    state: str
    eligibility: str = "Unclear"
    estimated_subsidy: str = ""
    explanation: str = ""
    conditions: str = ""
    matched_schemes: list = field(default_factory=list)


def retrieve_schemes(category: str, state: str, top_k: int = 3):
    """Category-first, then state-aware filtering, then TF-IDF ranking."""
    same_category = [e for e in SCHEMES if e["category"] == category]
    if not same_category:
        return [e for e in SCHEMES if e["category"] == "general"]

    applicable = [
        e for e in same_category
        if e["level"] == "central"
        or (e["level"] == "state" and state.lower() in e["scheme"].lower())
    ]
    if not applicable:
        applicable = same_category

    if len(applicable) <= top_k:
        return applicable

    texts = [e["text"] for e in applicable]
    matrix = _VECTORIZER.transform(texts)
    query_vec = _VECTORIZER.transform([f"{category} {state}"])
    sims = cosine_similarity(query_vec, matrix).flatten()
    top_idx = sims.argsort()[::-1][:top_k]
    return [applicable[i] for i in top_idx]


def _build_prompt(category: str, description: str, price: float, state: str, schemes) -> str:
    context_block = "\n".join(
        f"- [{s['scheme']} | {s['level']}] {s['text']} (source: {s['source_url']}, last verified {s['last_verified']})"
        for s in schemes
    )
    return f"""You are a cautious, responsible-AI assistant for green loan/subsidy eligibility in India.
Ground your answer ONLY in the scheme context below. Do NOT invent scheme names,
amounts, or deadlines not present in the context. If the context does not clearly
cover the user's item or state, say so explicitly rather than guessing.

Scheme context (retrieved):
{context_block}

User's planned purchase:
- Item category: {category}
- Description: {description}
- Price (INR): {price}
- State: {state}

Return ONLY a JSON object with exactly these keys:
{{
  "eligibility": "Likely Eligible" | "Partially Eligible" | "Not Covered" | "Unclear",
  "estimated_subsidy": "<amount or range from context, or 'Not specified in available schemes'>",
  "explanation": "<2-3 sentences, must reference only the schemes in the context above>",
  "conditions": "<key eligibility conditions from context, e.g. price caps, vendor requirements, deadlines>"
}}
"""


def _extract_json(raw: str) -> dict:
    """Robustly pull a JSON object out of an LLM response."""
    candidates = [raw]
    fenced = raw.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    candidates.append(fenced)
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    if match:
        candidates.append(match.group(0))

    for candidate in candidates:
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            continue

    return {
        "eligibility": "Unclear",
        "estimated_subsidy": "Could not parse model output",
        "explanation": "The model's response could not be parsed. Showing retrieved scheme context only.",
        "conditions": "",
    }


def check_eligibility(client: Groq, category: str, description: str, price: float, state: str) -> EligibilityResult:
    schemes = retrieve_schemes(category, state)
    prompt = _build_prompt(category, description, price, state, schemes)

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "Respond with valid JSON only, no markdown fences, no commentary before or after."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
            max_tokens=800,
        )
        raw = response.choices[0].message.content.strip()
        print(f"[SubsidySense] RAW MODEL OUTPUT:\n{raw}\n[END RAW OUTPUT]")
        parsed = _extract_json(raw)

        return EligibilityResult(
            item_category=category,
            description=description,
            price=price,
            state=state,
            eligibility=parsed.get("eligibility", "Unclear"),
            estimated_subsidy=parsed.get("estimated_subsidy", ""),
            explanation=parsed.get("explanation", ""),
            conditions=parsed.get("conditions", ""),
            matched_schemes=schemes,
        )

    except Exception as error:
        print(f"[SubsidySense] Groq call failed: {error!r}")
        return EligibilityResult(
            item_category=category,
            description=description,
            price=price,
            state=state,
            eligibility="Unclear",
            estimated_subsidy="Unable to determine",
            explanation="The AI service could not process this request right now. Please try again.",
            conditions="",
            matched_schemes=schemes,
        )