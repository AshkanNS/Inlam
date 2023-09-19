#program som beräknar medianen för ett antal värden

värden = []                 # Läs in värden från användaren och lagra dem i en lista
while True:
    inmatning = input("Ange ett värde (eller 'klart' för att avsluta): ")
    if inmatning.lower() == 'klart':
        break    
    try:
        värde = float(inmatning)
        värden.append(värde)
    except ValueError:
        print("Ogiltig inmatning. Ange ett giltigt numeriskt värde eller 'klart' för att avsluta.")

värden.sort()       # Sortera värdena i stigande ordning

n = len(värden)     # Beräkna medianen
if n % 2 == 1:
    median = värden[n // 2]
else:
    mitten_index1 = n // 2
    mitten_index2 = mitten_index1 - 1
    median = (värden[mitten_index1] + värden[mitten_index2]) / 2
print(f"Medianen av de inmatade värdena är: {median}")
