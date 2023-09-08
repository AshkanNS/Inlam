#Skriv ett program som läser in en cirkels radie. Programmet ska beräkna circkelns omkrets 
# och area och skriva ut de två resultaten på ett snyggt sätt med tre decimaler. 

import math

def radie (r):
    if r <= 0:
        return "Radien måste vara högre än 0"
    else:
        a = math.pi * r**2
        o = 2 * math.pi * r
        return f"Cirkelns area är: {a:.2f}\nCirkelns omkrets är: {o:.2f}"

for c in range (2):
    r = float(input ("Ange cirkelns radie: "))
    resultat = radie (r)
    print(resultat)
