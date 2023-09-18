#Skriv ett program som läser in ett godtyckligt antal positiva tal.
#När användaren skriver in ett negativt tal ska programmet skriva ut det största och det minsta av de positiva talen.

största = 0
minsta = 0 
while True:
    tal = float(input("skriv tal: "))
    if tal < 0:
        break
    if tal > största:
        största = tal
    if tal < minsta:
        minsta = tal
print (f"Största Talet: {största}")
print (f"Minsta talet: {minsta}")
