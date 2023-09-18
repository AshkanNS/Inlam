#vid början av år 2022 hade kommunen invånare invånare
#antalet födda och avlidna under ett år uppskattas vara 0.6-0.7% av befolkningen vid årets början
#skriv ett program beräknar kommunens uppskattade invånarantal 
#i början av ett visst år. vilket år ska anges som indata.

#kommunens informatin
invånare = 26000
uppskattad_födda = 0.07
uppskaddad_avlidna = 0.06
uppskattad_inflytt = 300
uppskattad_utflytt = 325

#ange år efter 2022
angivet_år = int(input("Vilket år: "))

if angivet_år >= 2022:
    år = angivet_år - 2022

    for i in range(1, år + 1):
        födda = invånare * uppskattad_födda
        avlidna = invånare * uppskaddad_avlidna
        utflytt = uppskattad_inflytt-uppskattad_utflytt
        invånare = invånare + födda - avlidna + utflytt

    print (f"Uppskattad antal invånare början av år {angivet_år}: {invånare:.0f}")
