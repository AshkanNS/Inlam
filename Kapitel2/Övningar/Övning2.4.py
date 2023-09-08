
#ange miles per gallon
mpg = float(input("Ange mpg: "))

#räkna ut 1 liter per mil från gallon
literpermil = 3.785 / mpg / 1.609 * 10

#skriv ut resultat
print (f"Förbrukning i l/mil {literpermil:.2f}")
