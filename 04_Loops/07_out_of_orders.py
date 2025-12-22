# Some chai flavors are out of stock.
# You want to skip those and stop entirely if
# someone requests a restricted flavor.
# Task:
# • Skip if flavor is "Out of Stock"
# • Break if flavor is "Discontinued"

flavours = ["Masala Chai", "Out of Stock", "Ginger Tea", "Discontinued", "Lemon Tea"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found")
        break
    

print(f"Out side of the loop")

