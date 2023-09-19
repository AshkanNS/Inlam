#program som beräknar standardavvikelsen av ett antal tal med en lista.
import math

talen = []

while True:
    inmatning = input("Ange ett tal (eller 'klart' för att avsluta): ")
    
    if inmatning.lower() == 'klart':
        break
    
    try:
        tal = float(inmatning)
        talen.append(tal)
    except ValueError:
        print("Ogiltig inmatning. Ange ett giltigt numeriskt värde eller 'klart' för att avsluta.")

medelvärde = sum(talen) / len(talen)
avvikelser_kvadrerade = [(tal - medelvärde) ** 2 for tal in talen]  # Beräkna avvikelserna från medelvärdet och kvadrera dem
medelvärde_kvadrerade = sum(avvikelser_kvadrerade) / len(talen)     # Beräkna medelvärdet av de kvadrerade avvikelserna
standardavvikelse = math.sqrt(medelvärde_kvadrerade)                # Beräkna standardavvikelsen genom att ta kvadratroten av medelvärdet av de kvadrerade avvikelserna

print(f"Standardavvikelsen är: {standardavvikelse:.2f}")
