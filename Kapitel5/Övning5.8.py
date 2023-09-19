#program som läser in två tidpunker o jämför hur många minuter det är mellan de.

tidpunkt1 = input("Ange den första tidpunkten (tt:mm): ")
tidpunkt2 = input("Ange den andra tidpunkten (tt:mm): ")

# Dela upp tidpunkterna i timmar och minuter
timmar1, minuter1 = map(int, tidpunkt1.split(":"))
timmar2, minuter2 = map(int, tidpunkt2.split(":"))

# Beräkna antalet minuter mellan tidpunkterna
totala_minuter1 = timmar1 * 60 + minuter1
totala_minuter2 = timmar2 * 60 + minuter2
differens_minuter = abs(totala_minuter2 - totala_minuter1)

# Skriv ut resultatet
print(f"Det är {differens_minuter} minuter mellan {tidpunkt1} och {tidpunkt2}.")
