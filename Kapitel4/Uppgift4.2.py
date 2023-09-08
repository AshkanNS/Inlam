## Om användaren anger 5 
#kommer koden att räkna summan av 1 + 2 + 3 + 4 + 5 = 15



n = int(input("n? "))
summa = 0
k = 1                       #koden räknar då 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 55
while k <= n:        #om vi tillsätter **2 bredvid k så ökas summan upphöjd
    summa = summa + k   #summan adderas då med k
    k = k + 1         #öka k med 1
print ("Summan blir", summa)