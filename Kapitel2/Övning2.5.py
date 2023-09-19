import math

#ange kordinater för o räkna ut avstånden mellan de
x1 = float(input("x1? "))
x2 = float(input("x2? "))
y1 = float(input("y1? "))
y2 = float(input("y2? "))
d= math.sqrt((x1-x2)**2 + (y1-y2)**2)
print (f"Avstånd: {d:.2f}")
