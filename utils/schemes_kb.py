"""
Curated green loan/subsidy scheme corpus for SubsidySense.

Every entry is sourced from an official government page or corroborated by
multiple independent, dated sources found via web search on 2026-09-17.
`last_verified` records when that sourcing happened, and `source_url` is
shown to the user alongside every AI answer so they can check it themselves.

IMPORTANT: Indian government subsidy schemes change frequently (deadlines
extended, amounts revised, schemes replaced). This corpus is a snapshot,
not a live feed. Treat every number here as "as reported at last_verified",
never as guaranteed-current.
"""

SCHEMES = [
    {
        "id": "pm-edrive-2w",
        "scheme": "PM E-DRIVE Scheme (Central)",
        "level": "central",
        "category": "ev_two_wheeler",
        "text": (
            "PM E-DRIVE is the central government's current EV demand-incentive scheme, "
            "launched 29 Sept 2024 as the successor to FAME-II (which ended 31 March 2024). "
            "For electric two-wheelers, the subsidy is Rs 2,500 per kWh of battery capacity, "
            "capped at Rs 5,000 per vehicle. Eligible vehicles must have an ex-factory price "
            "under Rs 1.5 lakh, carry PM E-DRIVE/testing-agency certification, and the subsidy "
            "window for two-wheelers has been reported to run until 31 July 2026 or until the "
            "vehicle quota (~24.79 lakh units) is exhausted, whichever comes first."
        ),
        "source_url": "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2152528",
        "last_verified": "2026-09-17",
    },
    {
        "id": "pm-edrive-3w",
        "scheme": "PM E-DRIVE Scheme (Central)",
        "level": "central",
        "category": "ev_three_wheeler",
        "text": (
            "PM E-DRIVE also covers electric three-wheelers (e-rickshaws, e-carts, L5 cargo "
            "EVs) with demand incentives, alongside e-trucks, e-ambulances, and grants for "
            "e-buses and charging infrastructure. Reported timelines vary by sub-category: "
            "e-rickshaw/e-cart incentives have been reported to continue to March 2028, while "
            "some cargo EV sub-incentives were reported to have ended in Dec 2025. The overall "
            "scheme outlay is Rs 10,900 crore."
        ),
        "source_url": "https://www.pib.gov.in/PressReleasePage.aspx?PRID=2152528",
        "last_verified": "2026-09-17",
    },
    {
        "id": "maharashtra-ev-2025",
        "scheme": "Maharashtra Electric Vehicle Policy 2025 (State)",
        "level": "state",
        "category": "ev_two_wheeler",
        "text": (
            "Maharashtra's EV Policy 2025 (effective 1 April 2025 to 31 March 2030, Rs 1,993 "
            "crore outlay) offers a purchase incentive of Rs 10,000 for electric two-wheelers "
            "for the first 1 lakh vehicles, on top of any central PM E-DRIVE incentive. All "
            "EVs registered in Maharashtra during the policy period get 100% exemption from "
            "motor vehicle tax and registration/renewal fees, plus toll exemption on select "
            "expressways (Mumbai-Pune, Samruddhi Mahamarg, Atal Setu)."
        ),
        "source_url": "https://mercomindia.com/maharashtra-targets-30-ev-adoption-by-2030-announces-purchase-sops",
        "last_verified": "2026-09-17",
    },
    {
        "id": "maharashtra-ev-2025-3w",
        "scheme": "Maharashtra Electric Vehicle Policy 2025 (State)",
        "level": "state",
        "category": "ev_three_wheeler",
        "text": (
            "Under Maharashtra's EV Policy 2025, electric three-wheelers get a purchase "
            "incentive of Rs 30,000 for the first 15,000 vehicles, in addition to any "
            "applicable central incentive, plus the same tax/registration/toll exemptions "
            "as other EV categories in the state."
        ),
        "source_url": "https://mercomindia.com/maharashtra-targets-30-ev-adoption-by-2030-announces-purchase-sops",
        "last_verified": "2026-09-17",
    },
    {
        "id": "maharashtra-ev-2025-car",
        "scheme": "Maharashtra Electric Vehicle Policy 2025 (State)",
        "level": "state",
        "category": "ev_four_wheeler",
        "text": (
            "Under Maharashtra's EV Policy 2025, private electric four-wheelers (cars) get a "
            "purchase incentive of Rs 1.5 lakh for the first 10,000 vehicles (some reports "
            "note the cap on private car subsidies was removed in this revision), and "
            "commercial electric four-wheelers can get up to Rs 2 lakh. Same tax, "
            "registration, and toll exemptions apply."
        ),
        "source_url": "https://svb1.cartoq.com/car-news/maharashtra-targets-one-in-three-new-vehicles-to-be-electric-by-2030",
        "last_verified": "2026-09-17",
    },
    {
        "id": "pm-surya-ghar",
        "scheme": "PM Surya Ghar: Muft Bijli Yojana (Central)",
        "level": "central",
        "category": "rooftop_solar",
        "text": (
            "PM Surya Ghar: Muft Bijli Yojana (launched Feb 2024, Rs 75,021 crore outlay, "
            "Ministry of New and Renewable Energy) gives Central Financial Assistance for "
            "residential rooftop solar: Rs 30,000 per kW for the first 2 kW, plus Rs 18,000 "
            "for the 3rd kW, capping total subsidy at Rs 78,000 for a 3 kW-or-larger system. "
            "Households also get up to 300 units of free electricity per month via net "
            "metering. Apply through the National Portal (pmsuryaghar.gov.in) using an "
            "MNRE-empanelled vendor and ALMM-listed modules; subsidy is credited to the bank "
            "account roughly 30-45 days after DISCOM inspection and commissioning."
        ),
        "source_url": "https://pmsuryaghar.gov.in",
        "last_verified": "2026-09-17",
    },
    {
        "id": "bee-star-appliance",
        "scheme": "BEE Star Labelling Programme (Central)",
        "level": "central",
        "category": "energy_efficient_appliance",
        "text": (
            "The Bureau of Energy Efficiency (BEE) Star Labelling Programme, run by the "
            "Ministry of Power, is NOT a direct cash subsidy — it is a mandatory energy-"
            "efficiency rating (1 to 5 stars) covering ACs, refrigerators, washing machines, "
            "fans, water heaters, and more. A higher star rating means lower running "
            "electricity cost and lower emissions, but a purchase rebate is not guaranteed "
            "nationally — some individual state DISCOMs or utility programs occasionally run "
            "their own appliance exchange/rebate schemes, which must be checked separately "
            "and are not covered in this corpus."
        ),
        "source_url": "https://www.beestarlabel.com",
        "last_verified": "2026-09-17",
    },
    {
        "id": "general-no-match",
        "scheme": "No specific scheme matched",
        "level": "general",
        "category": "general",
        "text": (
            "No specific central or state scheme in this corpus matches the item or state "
            "described. This does not mean no subsidy exists — it means this prototype's "
            "curated knowledge base does not cover it. Check the state's transport/energy "
            "department portal, or the national portals: pmsuryaghar.gov.in (solar) and the "
            "relevant state EV policy page."
        ),
        "source_url": "https://www.pib.gov.in",
        "last_verified": "2026-09-17",
    },
]
