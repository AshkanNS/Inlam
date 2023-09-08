#rekommenderar ifall man ska köpa engångsbiljetter eller årskort
# vid besök av gym

#infogad info
print ("Välkommen till NiniGym!!")
print ("Kostnaden för engångsbiljett är 80kr")
print ("Kostnaden för årskort är 7200kr")

besök = int(input("Hur ofta brukar du träna under ett år? "))
årskort = 7200
biljett = 80

kostnadperår = biljett * besök

if årskort < kostnadperår:
    print ("Det lönar sig att köpa ett årskort.")
else:
    print ("Du tjänar mer på att köpa engångsbiljett.")


