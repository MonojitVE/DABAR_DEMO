# data.py
# Mock unified financial data for DABAR demo

# Simulated transactions from multiple sources
transactions = [
    {
        "date": "2026-06-01",
        "description": "Salary Credit",
        "category": "Income",
        "source": "Bank Account",
        "amount": 60000
    },
    {
        "date": "2026-06-02",
        "description": "House Rent",
        "category": "Housing",
        "source": "Bank Account",
        "amount": -25000
    },
    {
        "date": "2026-06-03",
        "description": "Groceries",
        "category": "Food",
        "source": "Digital Wallet",
        "amount": -4500
    },
    {
        "date": "2026-06-05",
        "description": "Electricity Bill",
        "category": "Utilities",
        "source": "Mobile Money",
        "amount": -3200
    },
    {
        "date": "2026-06-07",
        "description": "Internet Bill",
        "category": "Utilities",
        "source": "Mobile Money",
        "amount": -1800
    },
    {
        "date": "2026-06-10",
        "description": "Freelance Payment",
        "category": "Income",
        "source": "Digital Wallet",
        "amount": 60000
    }
]

# Dashboard summary (used for analytics + AI context)
def dashboard_summary():
    total_income = sum(t["amount"] for t in transactions if t["amount"] > 0)
    total_expenses = abs(sum(t["amount"] for t in transactions if t["amount"] < 0))
    balance = total_income - total_expenses

    category_breakdown = {}
    for t in transactions:
        if t["amount"] < 0:
            category = t["category"]
            category_breakdown[category] = category_breakdown.get(category, 0) + abs(t["amount"])

    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "balance": balance,
        "top_expense_category": max(category_breakdown, key=category_breakdown.get),
        "category_breakdown": category_breakdown
    }