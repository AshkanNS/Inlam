#program som läser in personnummer och gratulerar vid födelsedag.

import datetime

nr = input ("Ange pnr (ååmmdd): ")   
dt  = datetime.datetime.now()   #hämtar dagens datum o tid
s = str(dt.date())  #konverterar dagens datum till en sträng

if nr [2: 4] == s[5: 7] and nr [4:6] == s[8:]:  # Jämför de två delarna av personnumret med dagens månad och dag.
                                                # Om de är lika, skrivs en födelsedagshälsning, 
    print ("Grattis på din födelsedag", s)
else:
    print ("Det var inte din födelsedag")       # annars skriv ut att det inte är födelsedagen.
