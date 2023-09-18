#program som räknar ut hur länge man behöver arbeta för att tjäna 10 miljoner
#första dagen tjänar man ett öre och sedan fördubblas lönen varje dag

totallön = 0.1  #startlön på 1 öre
antaldagar = 0

while totallön < 10000000:  # Loopa tills du tjänar 10 miljoner
    totallön *= 2           # Beräkna dagens lön (dubbla lönen varje dag)
    antaldagar += 1         # Öka antal dagar med 1

print(f'Det tar {antaldagar} dagar att tjäna 10 miljoner.')