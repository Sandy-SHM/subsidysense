# 🔋 SubsidySense — Green Loan/Subsidy Eligibility Advisor

An AI-powered advisor that checks whether an EV, rooftop solar, or energy-efficient appliance purchase qualifies for real Indian government subsidies — built for the **1M1B AI for Sustainability Virtual Internship** (IBM SkillsBuild & AICTE).

**SDG Alignment:** Primary — SDG 7 (Affordable & Clean Energy). Secondary — SDG 12, SDG 13.

🔗 **Live demo:** https://subsidysensebranchmain-hjcv9u6mcnxvphixcggbqj.streamlit.app/
📂 **GitHub:** https://github.com/Sandy-SHM/subsidysense

---

## The problem

People financing an EV, solar setup, or energy-efficient appliance rarely know which government subsidies they actually qualify for — schemes are scattered across central (PM E-DRIVE, PM Surya Ghar) and state-level policies, with different amounts, caps, and deadlines. Most people either miss free money or don't factor it into their loan decision.

## How it works

1. **Retrieve** — TF-IDF search over a curated, sourced knowledge base of real government schemes, filtered by item category and state
2. **Augment** — the retrieved scheme text is inserted into the prompt as grounding context
3. **Generate** — a Groq-hosted LLM (`openai/gpt-oss-120b`) returns a structured eligibility verdict: status, estimated subsidy, explanation, conditions
4. **Present** — every answer shows its exact source link and a mandatory "verify before applying" disclaimer, since scheme details change over time

This is a Retrieval-Augmented Generation (RAG) pipeline — the model is only allowed to use facts it was just given, not invent numbers from memory.

## Tech stack

- Streamlit (UI)
- Groq API (`openai/gpt-oss-120b`)
- scikit-learn (TF-IDF retrieval)
- python-dotenv (local config)

## Data sources

Scheme details are sourced from official/verified pages as of Sept 2026:
- PM E-DRIVE — pib.gov.in
- PM Surya Ghar: Muft Bijli Yojana — pmsuryaghar.gov.in
- Maharashtra EV Policy 2025 — mercomindia.com
- BEE Star Labelling Programme — beestarlabel.com

⚠️ Indian government schemes change frequently. This is a dated snapshot, not a live feed — always verify current numbers on the official portal before applying.

## Setup (run locally)

```bash
git clone https://github.com/Sandy-SHM/subsidysense.git
cd subsidysense
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Get a free Groq API key at https://console.groq.com/keys, then create a `.env` file:

```bash
printf 'GROQ_API_KEY=your_key_here\n' > .env
```

Run it:

```bash
streamlit run app.py
```

## Project structure
