talent = float(input("Enter talents: "))
pound = float(input("Enter pounds: "))
lot = float(input("Enter lots: "))
mass = ((talent * 20 + pound) * 32 + lot) * 13.3
mass_kg = int(mass // 1000)
mass_gr = mass % 1000
print("The weight in modern units:", mass_kg, f"kilograms and {mass_gr:.2f} grams")