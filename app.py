import os

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

from utils.analyzer import check_eligibility

load_dotenv()

st.set_page_config(page_title="SubsidySense - Green Loan/Subsidy Advisor", page_icon="🔋", layout="wide")

st.title("🔋 SubsidySense")
st.caption(
    "A Green Loan/Subsidy Eligibility Advisor — AI for Sustainability Internship Project "
    "(SDG 7: Affordable & Clean Energy)"
)

api_key = os.getenv("GROQ_API_KEY", "")

with st.sidebar:
    if not api_key:
        st.error("GROQ_API_KEY not found. Add it to your .env file and restart the app.")
    st.subheader("Responsible AI Notes")
    st.caption(
        "Every answer is grounded in a curated, dated scheme snapshot and shows its exact "
        "source. Government schemes change — always verify on the official portal before "
        "applying or financing a purchase."
    )

CATEGORY_LABELS = {
    "ev_two_wheeler": "Electric two-wheeler (scooter/bike)",
    "ev_three_wheeler": "Electric three-wheeler (rickshaw/cart)",
    "ev_four_wheeler": "Electric four-wheeler (car)",
    "rooftop_solar": "Rooftop solar system",
    "energy_efficient_appliance": "Energy-efficient appliance (AC, fridge, etc.)",
}
STATES = ["Maharashtra", "Delhi", "Karnataka", "Gujarat", "Tamil Nadu", "Other / Not listed"]

st.subheader("1. What are you planning to finance?")

col1, col2, col3 = st.columns(3)
with col1:
    category_label = st.selectbox("Item category", list(CATEGORY_LABELS.values()))
    category = [k for k, v in CATEGORY_LABELS.items() if v == category_label][0]
with col2:
    price = st.number_input("Price / loan amount (INR)", min_value=0, value=120000, step=5000)
with col3:
    state = st.selectbox("State", STATES)

description = st.text_input("Brief description (model, capacity, etc.)", placeholder="e.g. Ather 450X electric scooter, 3 kWh battery")

st.subheader("2. Check eligibility")

if st.button("Check Green Subsidy Eligibility", type="primary", disabled=not api_key):
    client = Groq(api_key=api_key)
    with st.spinner("Retrieving matching schemes and checking eligibility..."):
        result = check_eligibility(client, category=category, description=description, price=float(price), state=state)
    st.session_state.result = result

if not api_key:
    st.info("Enter your Groq API key in the sidebar to run a check.")

if "result" in st.session_state:
    r = st.session_state.result
    badge = {
        "Likely Eligible": "🟢",
        "Partially Eligible": "🟡",
        "Not Covered": "🔴",
        "Unclear": "⚪",
    }.get(r.eligibility, "⚪")

    st.subheader("3. Result")
    st.markdown(f"### {badge} {r.eligibility}")
    st.write(f"**Estimated subsidy:** {r.estimated_subsidy}")
    st.write(f"**Explanation:** {r.explanation}")
    if r.conditions:
        st.write(f"**Key conditions:** {r.conditions}")

    st.markdown("---")
    st.markdown("**Sources this answer was grounded in — verify before applying:**")
    for s in r.matched_schemes:
        st.markdown(f"- **{s['scheme']}** — [{s['source_url']}]({s['source_url']}) · last checked {s['last_verified']}")

    st.warning(
        "⚠️ Subsidy amounts, deadlines, and eligibility conditions for Indian government "
        "schemes change frequently and without notice. This is an AI-assisted estimate from "
        "a curated snapshot, not a guarantee. **Verify current numbers on the official "
        "portal linked above before applying or signing any loan.**"
    )

st.markdown("---")
st.caption(
    "Built for the 1M1B AI for Sustainability Virtual Internship (IBM SkillsBuild & AICTE). "
    "Prototype only — not financial or legal advice."
)
