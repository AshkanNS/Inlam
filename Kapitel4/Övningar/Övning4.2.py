#program som skriver ut en tabell för talen 1 till 12.
#på varje rad i tabellen ska talet visas liksom talet i kvadrat och talet i kubik.


for x in range (1, 13): #tabell från 1-12
    kvadrat = x**2      #i kvadrat
    kubik = x**3        #i kubik

    print(f"Tabell: {x:1}{kvadrat:5.0f}{kubik:5.0f}")
