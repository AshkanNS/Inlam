

#x = int(input("vår värde: "))
print ("2 * x**2 - 5 * x + 1 ")

for x in range (-10, 11):   #vårt tabell avstånd ända från -10 upp till 11
    summa = 2 * x**2 - 5 * x + 1 
 
    print (f"Tabell: {x:2}{summa:5.0f}")    #skriver ut en tabell parallelt