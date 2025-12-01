# BOOLEAN

is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling  # Upcasting
print(f"Total actions (with boolean upcasting): {total_actions}")

milk_present = False
print(f"Is milk present? {bool(milk_present)}")

water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Can we serve tea? {can_serve}")