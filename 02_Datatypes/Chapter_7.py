masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cadarmom_ratio = 2, 1
print(f"Ratio is G:{ginger_ratio} and C:{cadarmom_ratio}")
ginger_ratio, cadarmom_ratio = cadarmom_ratio, ginger_ratio
print(f"Ratio is G:{ginger_ratio} and C:{cadarmom_ratio}")

# membership testing

print(f"Is cinnamon a masala spice? {'cinnamon' in masala_spices}")