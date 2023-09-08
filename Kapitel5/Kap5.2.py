import datetime

nr = input ("Ange pnr: ")
dt  = datetime.datetime.now()
s = str(dt.date())

if nr [2: 4] == s[5: 7] and nr [4:6] == s[8:]:
    print ("Grattis på din födelsedag", s)
else:
    print ("Det var inte din födelsedag")
