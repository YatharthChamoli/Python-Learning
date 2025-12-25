# Improving Readability
# You sell different chai sizes.
# Instead of writing formulas everywhere, create a function.
# Task:
# • Write calculate_bill(cups, price_per_cup)
# • Return total bill
# • Use this function for multiple orders

def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bill(3, 5)
print(f"My bill is: ${my_bill}")