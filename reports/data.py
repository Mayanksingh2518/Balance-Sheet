assets = [
    {"Account": "Cash", "Amount": 50000},
    {"Account": "Accounts Receivable", "Amount": 30000},
    {"Account": "Inventory", "Amount": 20000},
]
liabilities = [
    {"Account": "Accounts Payable", "Amount": 25000},
    {"Account": "Loans Payable", "Amount": 15000},
]
equity = [
    {"Account": "Owner's Capital", "Amount": 60000},
]

totals = {
    "assets": sum(x["Amount"] for x in assets),
    "liabilities": sum(x["Amount"] for x in liabilities),
    "equity": sum(x["Amount"] for x in equity),
}
