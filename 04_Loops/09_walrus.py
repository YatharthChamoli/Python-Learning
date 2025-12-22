# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

value = 13

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")


available_sizes = ["S", "M", "L", "XL"]

if(size := input("Enter size (S, M, L, XL): ")) in available_sizes:
    print(f"Size {size} is available")
else:
    print(f"Size {size} is not available")    


flavors = ["masala", "ginger", "lemon", "cardamom"]

print("Available flavors:")

while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available.")
    
print(f"Great! {flavor} is available.")    