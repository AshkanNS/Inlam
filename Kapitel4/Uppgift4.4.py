#hur många gånger studsar bollen innan den blir helt stilla
#bollen förlorar 30% höjd vid varje studs

höjd_meter = float(input("Ange från vilken höjd(meter) du släpper bollen: "))

studs = 0

while höjd_meter > 0.01:    #om bollen studsar högre än 1 cm
    höjd_meter *= 0.7       #formel för bollen förlorar 30% vid varje studs
    studs = studs +1        #räknar för varje bollar studsar
print (f"Bollen hinner studsa {studs} gr")

