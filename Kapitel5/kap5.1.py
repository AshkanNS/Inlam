
s = input("Skriv en mening: ")
s = s.strip()
i = s.find(" ")
j = s.rfind(" ")
print("Det första ordet är:", s[0:i])
print("Det sista ordet är: ", s[j+1:])
