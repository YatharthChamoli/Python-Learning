staff = [("John", 16), ("Jane", 22), ("Doe", 19)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff.")
        break
else:
    print("No staff member is eligible to manage the staff.")    