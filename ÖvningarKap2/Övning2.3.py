
#ange hur många farenheit som du vill översätta till celsius
fahrenheit = (float(input("Skriv temperatur i fahrenheit: ")))

#formel för jämna ut celsius med fahrenheit
celsius = (fahrenheit - 32) * 5 / 9

#skriv ut resultat
print (f"temperaturen i celsius {celsius:.1f}")
