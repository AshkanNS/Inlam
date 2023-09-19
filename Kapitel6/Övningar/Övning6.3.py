#programmet jämför en lista och tuple för att se om de är lika


l = input("Skriv en lista: ").split()
t = tuple(input("Skriv en tupel: ").split())
if l == t:                                      # Jämför om den inlästa listan (l) är lika med den inlästa tupeln (t)
    print("Ska aldrig hända")                                  
l2 = list(t)                                    # Skapa en lista (l2) från tupeln (t)
if l == l2:                                     # Jämför om den inlästa listan (l) är lika med den omvandlade listan (l2)
    print("Lika") 
else:
    print("Olika")
