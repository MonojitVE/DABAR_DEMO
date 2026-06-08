import os
from openai import OpenAI
from dotenv import load_dotenv
from data import dashboard_summary

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(question: str):
    summary = dashboard_summary()

    prompt = f"""
You are a financial assistant.

Here is the user's financial summary:
- Total income: ₹{summary['total_income']}
- Total expenses: ₹{summary['total_expenses']}
- Balance: ₹{summary['balance']}
- Top expense category: {summary['top_expense_category']}

User question:
{question}

Explain clearly in simple language and return the answer in markdown format strictly.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",   # ✅ STABLE, FAST, CHEAP
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content