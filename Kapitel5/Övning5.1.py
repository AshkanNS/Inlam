#programmet ska läsa in en mening (minst två ord), sedan visa ett meddelande 
#som säger hur många tecken som skrivits och vilket första o sista ordet vart.

# skriva en mening 
s = input("Skriv en mening: ").strip()
# Hittar indexet för det första mellanslaget i strängen.
i = s.find(" ")
# Hittar indexet för det sista mellanslaget i strängen (räknar bakåt från slutet).
j = s.rfind(" ")

# Skriver ut det första ordet i strängen baserat på positionen före det första mellanslaget.
print("Det första ordet är:", s[0:i])
# Skriver ut det sista ordet i strängen baserat på positionen efter det sista mellanslaget.
print("Det sista ordet är: ", s[j+1:])
