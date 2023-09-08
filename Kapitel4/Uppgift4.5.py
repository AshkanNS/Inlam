#hur många gånger studsar bollen innan den blir helt stilla
#bollen förlorar 30% höjd vid varje studs, samma uppgift som 4.4 fast upprepande kod

#while True kör koden upprepande så angivet tal är inom ramen
while True:
    höjd_meter = float(input("Ange från vilken höjd(meter) du släpper bollen: "))
    if höjd_meter <= 0:
        break   #koden stoppas ifall angivet tal är fel, negativt i detta fall
    studs = 0
    while höjd_meter > 0.01:
        höjd_meter *= 0.7
        studs = studs +1
    print (f"Bollen hinner studsa {studs} gr")

