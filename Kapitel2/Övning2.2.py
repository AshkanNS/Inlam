import math #tillsatt bibliotek

#räknar angiven radie till volym och area
r = float (input('radie'))
v = 4* math.pi * r**3 / 3
a = 4* math.pi * r**2 

#skriv ut resultat
print ("Volymen är", v)
print ("Area är:", a)