import math

t = int(input("Antal år?"))
lam = math.log (2.0) / 5730
rest = 100 * math.exp(-lam * t)

print (f"Det återstår {rest:.2f} %")