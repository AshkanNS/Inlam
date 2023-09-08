#program som läser in varans pris och anger ink/ex moms

# Läs in priset inklusive moms och momssatsen i procent
prisink = float(input("Ange priset ink moms: "))
momsen = float(input("Ange momsen i procent: "))

# Beräkna momsen
moms = (prisink * momsen) / 100

# Beräkna priset exklusive moms
prisex = prisink - moms

# Skriv ut resultaten
print(f"Priset exklusive moms är: {prisex:.2f} kr")
print(f"Momsen är: {moms:.2f} kr")