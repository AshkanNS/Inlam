## Om användaren anger 5 
#kommer koden att räkna summan av 1 + 2 + 3 + 4 + 5 = 15


n = int(input("n? "))
summa = 0
                     
for k in range (1, n+1):               
    summa = summa + k   #summan adderas då med k
print ("Summan blir", summa)