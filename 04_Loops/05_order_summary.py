# You're preparing an order summary with customer names
# and their total bill.
# Task:
# • Use two lists: one for names and one for bills.
# • Print: "[Name] paid ₹[amount]"

names = ["Amit", "Bina", "Chirag", "Divya", "Esha"]
bills = [150, 200, 250, 300, 350]

for name, amount in zip(names, bills):
    print(f"{name} paid ₹{amount}")