#programmet avgör om angivet personnummer är man eller kvinna

import datetime

nr = input("skriv ett personnummer: ")
siff = int(nr[-2])  # Extraherar den sista siffran i personnumret och konverterar den till ett heltal.
if siff % 2 == 0:   # Kontrollerar om den sista siffran är jämn eller udda för att avgöra kön.
    print("Kvinna")
else:
    print("Man")


    