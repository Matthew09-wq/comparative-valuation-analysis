"""
Comparative Valuation Analysis
Microsoft, Adobe and Netflix

Market snapshot: 9 September 2026

This public-safe script reproduces the core valuation calculations
used in the portfolio case study without relying on proprietary
source datasets.
"""

# =========================================================
# PUBLIC CASE-STUDY INPUTS
# USD millions except share price and percentages
# =========================================================

companies = {
    "Microsoft": {
        "ticker": "MSFT",
        "share_price": 491.65,
        "market_cap": 3650769.0,
        "enterprise_value": 3702739.0,
        "ltm_revenue": 331839.0,
        "ltm_operating_income": 155237.0,
        "ltm_net_income": 133749.0,
        "ltm_free_cash_flow": 66987.0,
        "revenue_growth_pct": 17.79,
        "operating_margin_pct": 46.78,
        "net_margin_pct": 40.31,
        "fcf_margin_pct": 20.19,
        "net_cash_debt_bn": 36.55,
        "debt_to_equity": 0.09,
    },
    "Adobe": {
        "ticker": "ADBE",
        "share_price": 254.86,
        "market_cap": 101310.0,
        "enterprise_value": 102760.0,
        "ltm_revenue": 25198.0,
        "ltm_operating_income": 9090.0,
        "ltm_net_income": 7229.0,
        "ltm_free_cash_flow": 10280.0,
        "revenue_growth_pct": 11.49,
        "operating_margin_pct": 36.07,
        "net_margin_pct": 28.69,
        "fcf_margin_pct": 40.80,
        "net_cash_debt_bn": 0.38,
        "debt_to_equity": 0.53,
    },
    "Netflix": {
        "ticker": "NFLX",
        "share_price": 76.03,
        "market_cap": 316584.0,
        "enterprise_value": 324111.0,
        "ltm_revenue": 48370.764,
        "ltm_operating_income": 14354.517,
        "ltm_net_income": 13649.642,
        "ltm_free_cash_flow": 11152.005,
        "revenue_growth_pct": 16.02,
        "operating_margin_pct": 29.68,
        "net_margin_pct": 28.22,
        "fcf_margin_pct": 23.06,
        "net_cash_debt_bn": -5.40,
        "debt_to_equity": 0.54,
    },
}


# =========================================================
# VALUATION FUNCTIONS
# =========================================================

def pe_ratio(market_cap, net_income):
    return market_cap / net_income


def ev_to_revenue(enterprise_value, revenue):
    return enterprise_value / revenue


def ev_to_ebit(enterprise_value, operating_income):
    return enterprise_value / operating_income


def price_to_fcf(market_cap, free_cash_flow):
    return market_cap / free_cash_flow


def fcf_yield(market_cap, free_cash_flow):
    return free_cash_flow / market_cap * 100


def calculate_valuation(data):
    return {
        "P/E": pe_ratio(
            data["market_cap"],
            data["ltm_net_income"]
        ),
        "EV/Revenue": ev_to_revenue(
            data["enterprise_value"],
            data["ltm_revenue"]
        ),
        "EV/EBIT": ev_to_ebit(
            data["enterprise_value"],
            data["ltm_operating_income"]
        ),
        "P/FCF": price_to_fcf(
            data["market_cap"],
            data["ltm_free_cash_flow"]
        ),
        "FCF Yield": fcf_yield(
            data["market_cap"],
            data["ltm_free_cash_flow"]
        ),
    }


# =========================================================
# OUTPUT
# =========================================================

def print_results():
    print("Comparative Valuation Analysis")
    print("Market snapshot: 9 September 2026")
    print()

    for company, data in companies.items():
        valuation = calculate_valuation(data)

        print(f"{company} ({data['ticker']})")
        print(f"  P/E:         {valuation['P/E']:.2f}x")
        print(f"  EV/Revenue:  {valuation['EV/Revenue']:.2f}x")
        print(f"  EV/EBIT:     {valuation['EV/EBIT']:.2f}x")
        print(f"  P/FCF:       {valuation['P/FCF']:.2f}x")
        print(f"  FCF Yield:   {valuation['FCF Yield']:.2f}%")
        print()


# =========================================================
# QA CHECKS
# =========================================================

expected = {
    "Microsoft": {
        "P/E": 27.30,
        "EV/Revenue": 11.16,
        "EV/EBIT": 23.85,
        "P/FCF": 54.50,
        "FCF Yield": 1.83,
    },
    "Adobe": {
        "P/E": 14.01,
        "EV/Revenue": 4.08,
        "EV/EBIT": 11.30,
        "P/FCF": 9.86,
        "FCF Yield": 10.15,
    },
    "Netflix": {
        "P/E": 23.19,
        "EV/Revenue": 6.70,
        "EV/EBIT": 22.58,
        "P/FCF": 28.39,
        "FCF Yield": 3.52,
    },
}


def run_checks(tolerance=0.02):
    print("QA Checks")

    all_passed = True

    for company, expected_values in expected.items():
        actual = calculate_valuation(companies[company])

        company_passed = True

        for metric, expected_value in expected_values.items():
            if abs(actual[metric] - expected_value) > tolerance:
                company_passed = False
                all_passed = False

        status = "PASS" if company_passed else "FAIL"
        print(f"{company}: {status}")

    print()
    print(
        "All valuation checks passed."
        if all_passed
        else "One or more valuation checks failed."
    )


if __name__ == "__main__":
    print_results()
    run_checks()
