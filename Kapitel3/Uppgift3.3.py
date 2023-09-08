#matteprov högst 50 poäng lägst 25 betyg 
#från A till E med 5 poäng i marginal

poäng = int(input("Ange din poäng: "))

betyg = [("E", 25), ("D", 30), ("C", 35), ("B", 40), ("A", 45)]

# Hitta vilket betyg som matchar elevens poäng
resultat = None

for betyg, min_poäng in betyg:
    if poäng >= min_poäng:
        resultat = betyg
    else:
        break

# Visa resultatet
if resultat:
    print(f"Ditt betyg är: {resultat}")
else:
    print("Ogiltiga poäng. Ange poäng mellan 25 och 50.")


