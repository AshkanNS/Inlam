
s = input ("skriv ett antal heltal: ")
ls = s.split()
tal = [int(e) for e in ls]  # Konvertera varje delsträng (heltal) till ett heltal och lagra dem i en lista

for i in range (0, len(tal)):
    if not tal[i] in tal[0:i]:  # Kontrollera om det aktuella talet inte finns i listan med tidigare lästa tal
        print(tal[i], end=" ")  # Om talet är unikt, skriv ut det och använd "end" för att undvika ny rad efter varje tal


# s = (input("Skriv flera heltal: ").split())

#for i in range (0, len(s)):
#    if not s[i] in s[0:i]:
#        print (str (s[i]), end=" ")
