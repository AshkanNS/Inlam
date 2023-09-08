import math
#läs in längden på två sidor av en triangel och vinkeln mellan sidorna
a = float(input("Ange längd på sida A: "))
b = float(input("Ange längd på sida B: "))
v = float(input("Ange Vinkeln mellan sidorna A o B: "))
vlängd = math.radians(v)    #uträkning för vinkelns längd
c = math.sqrt (a**2 + b**2 - 2 * a * b * math.cos (vlängd))

#koden avgör ifall triangeln är de olika nämnarna
if a == b == c:
    print ("Triangeln är liksidig")
elif a == b or a == c or b == c:
    print ("Triangeln är likbent")
else:
    print ("Triangeln är oliksidig")
