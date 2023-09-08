# Skapa en tabell med värden för uttrycket 2x^2 - 5x + 1 för specifika x-värden
print(" x   |   2x^2 - 5x + 1")
print("-----------------------")

x_values = [0, 0.1, -0.9, -1]  # Ange de specifika x-värden

for x in x_values:
    resultat = 2 * x**2 - 5 * x + 1
    print(f"{x:.1f}  |   {resultat:.2f}")
