#om vi anger 5 kommer koden 
#att räkna 1/1 + 1/2 + 1/3 + 1/4 + 1/5 = 2.283333333333333

n = int(input("n? "))
summa = 0
k = 1
while k <= n:
    summa = summa + 1 / k  #summan ökas då med k
    k = k + 1        #öka k med 1
print (f"Summan blir {summa:.2f}")