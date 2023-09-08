
pnr = input("Ange pnr: ").strip()
j_tal = "02468"
flag = 0

if pnr[-2] in j_tal:
        flag = 1

if flag:
    print ("Jämnt")
else:
    print ("Udda")
