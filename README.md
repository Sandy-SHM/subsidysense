# SubsidySense - Green Loan/Subsidy Eligibility Advisor

1M1B AI for Sustainability Virtual Internship project. SDG 7 (Affordable & Clean Energy).

## Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Get a free Groq key at https://console.groq.com/keys, paste into sidebar or .env

## Run
streamlit run app.py

## What it does
Pick an item (EV, solar, appliance), price, state. RAG retrieves matching
government scheme snippets (sourced from PIB, pmsuryaghar.gov.in, state EV
policy reports), grounds a Groq LLM's eligibility verdict in them, and shows
the exact source link + a mandatory "verify before applying" disclaimer.
