# Ett program som läser in antalet minuter kunden uppskattar att de kommer att ringa per månad.
# programmet rekommenderar vilket abonnemang man bör välja.

min = int(input ("Hur många minuter ringer du per månad? "))

# om samtalet är 33 minuter eller mindre
if min <= 33:
    print ("Vi rekommenderar Kontant abonnemang")
# om samtalet är mellan 33 och 66 minuter
elif min <= 66: 
    print ("Vi rekommenderar Normal abonnemang")
# om samtalet är längre än 66 minuter
else:
    min > 66
    print ("Vi rekommenderar Plus abonnemang")

