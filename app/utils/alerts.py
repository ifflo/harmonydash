# app/utils/alerts.py
from .financial_analysis import analyze_financial_data


def check_budget_thresholds():
    category_totals = analyze_financial_data()
    if category_totals is None:
        return "Error in fetching transactions."

    alerts = []
    # Example: Check if any category exceeds a certain threshold
    for category, total in category_totals.items():
        if total > 50:  # Define your threshold
            alerts.append(f"Budget exceeded for {category}.")

    return alerts
