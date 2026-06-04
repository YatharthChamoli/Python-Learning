# Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = input("Enter your pet's species (Dog/Cat): ")
age = int(input("Enter pet age: "))

if species == "Dog":
    if age < 2:
        print("Puppy Food")
    else:
        print("Adult Dog Food")
elif species == "Cat":
    if age > 5:
        print("Senior Cat Food")
    else:
        print("Adult Cat Food")
else:
    print("Invalid Species!")                        