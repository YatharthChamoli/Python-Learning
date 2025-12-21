# You're creating a tea menu board.
# Each item must be numbered.
# Task:
# • Use enumerate() to print menu items with numbers.

menu = ["Masala Chai", "Ginger Tea", "Lemon Tea", "Green Tea", "Black Tea"]

for idx, item in enumerate(menu, start=1):
    print(f"{idx}: {item} chai")