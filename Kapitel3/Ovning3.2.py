import math

#Skriv ett program som läser in en cirkels radie. Programmet ska beräkna circkelns omkrets 
# och area och skriva ut de två resultaten på ett snyggt sätt med tre decimaler. 

r = float(input ("Ange cirkelns radie: "))
a = 4 * math.pi * r**2      # pi gånger radie upphöjt till två
o = 2 * math.pi * r

#kontrollerar att den inmatade radien är högre än 0 
if r <= 0:
    print ("Fel, talet måste vara högre än 0")
elif r >= 1:
    print (f"Area: {a:.3f}")
    print (f"Omkrets: {o:.3f}")
