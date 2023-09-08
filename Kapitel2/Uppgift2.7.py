import math

#skriv ett program som läser in en cirkels radie. Programmet ska beräkna cirkelns omkrets 
#och area och skriva ut de två resultaten med 3 decimaler

r = (float(input("Ange cirkelns radie: ")))

#uträkning för omkreat och area
omkrets = 2 * math.pi * r
area = math.pi * r **2

#visar resultat
print (f"Arean är: {area:.2f}, Omkretsen är: {omkrets:.2f}")