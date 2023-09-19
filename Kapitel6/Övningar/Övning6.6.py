# Läs in antalet rader och kolumner i matrisen från användaren
rader = int(input("Ange antal rader i matrisen: "))
kolumner = int(input("Ange antal kolumner i matrisen: "))

# Skapa en tom matris som en tvådimensionell lista
matris = []

print("Ange matriselementen:")
for i in range(rader):
    rad = input().split()
    if len(rad) != kolumner:
        print("Fel antal element i raden. Ange igen.")
        exit(1)                     # Avsluta programmet om antalet element i raden är felaktigt
    rad = [int(element) for element in rad]
    matris.append(rad)

är_symmetrisk = True                # Kontrollerar om matrisen är symmetrisk
for i in range(rader):
    for j in range(i, kolumner):
        if matris[i][j] != matris[j][i]:
            är_symmetrisk = False
            break

if är_symmetrisk:
    print("Matrisen är symmetrisk.")
else:
    print("Matrisen är inte symmetrisk.")
