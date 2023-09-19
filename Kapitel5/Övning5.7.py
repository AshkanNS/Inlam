#program som läser in amerikansk stil av å ä ö o översätter till svenska

# texten läses in med små bokstäver för o förenkla översättningen
text = input("Ange en text: ").lower()

# Ersätter "aa" med "å" m.m
text = text.replace("aa", "å")
text = text.replace("ae", "ä")
text = text.replace("oe", "ö")

# Skriv ut den översatta texten
print("Översatt text:", text)
