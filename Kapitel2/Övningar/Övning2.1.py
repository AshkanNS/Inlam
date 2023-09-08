
#ange info om aktuell mätarställning
milidag = (int(input("Mätarställning idag? "))) 
#ange info för mätarställning för ett år sedan
milettår = (int(input("Mätarställning för ett år sedan? ")))
#ange hur många liter bensin som förbrukats
literbensin = float(input("Hur många liter bensin har förbrukats? "))

#beräknar total mil som körts på ett år
antalmil = milidag - milettår

#räknar ut snitt förbrukning per mil
förbrukning = literbensin / antalmil 

#visar resultat
print ("Antal körda mil: ", antalmil)
print ("Antal liter bensin: ", literbensin)
#tillagd float för att endast visa två decimaler
print(f"Förbrukning per mil: {förbrukning:.2f}")

