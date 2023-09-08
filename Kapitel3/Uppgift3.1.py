#programmet ska beräkna kostnaden för att ringa med ett abonnemang och hur många minter man ringer per månad
#vad det kostar per minut, 10% rabatt om man ringer för minst 300kr

minuter = float(input("Hur många minuter pratar du per månad? "))
kostnadpermin = float(input("Vad är kostnaden per minut? "))

pris = kostnadpermin * minuter

if pris >= 300:
    pris = pris * 0.9
    print (f"Du har fått 10% rabatt, Din totala kostnad är nu: {pris:.2f}")
else:
    print (f"Din totala kostnad är: {pris:.2f}")
