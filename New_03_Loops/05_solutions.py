# Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

input_Str = "teeter"

for char in input_Str:
    print(char)
    if input_Str.count(char) == 1:
        print("Char is: ", char)
        # break
