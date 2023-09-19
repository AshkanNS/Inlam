

summa = 0            # summan av serien
i = 0                # räknare för att hålla reda på vilket bråk-tal vi är på
bråk = 1             # variabeln med värdet av det aktuella bråket.
slutvärde = 0.00001  # loopen avslutas när termen har ett belopp mindre än angivet

while abs(bråk) >= slutvärde:
  summa += bråk
  i += 1
  bråk = (-1) ** i * (1 / i) 

print(f'Summan av serien är ungefär {summa}')