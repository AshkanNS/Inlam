#program som läser in en text och översätter den till rövarspråket

# Lista med vokaler som används för att identifiera konsonanter
vokaler = "aeiouyåäöAEIOUYÅÄÖ"

text_input = input("Skriv in en text: ")

oversatt_text = ""  # Sträng för att lagra översättningen till rövarspråket

# Loopa igenom varje tecken i den inmatade texten
for tecken in text_input:
    if tecken.isalpha():    # Om tecknet är en bokstav (och inte ett mellanslag eller liknande)
        if tecken not in vokaler:
            oversatt_text += tecken + "o" + tecken  # Lägg till bokstaven "o" följt av sig själv i den översatta texten
        else:
            oversatt_text += tecken  # Om bokstaven är en vokal, lägg bara till den i den översatta texten
    else:
        oversatt_text += tecken # Om tecknet inte är en bokstav (t.ex. mellanslag eller skiljetecken),
                                # lägg bara till det i den översatta texten som det är

print("Översatt till rövarspråket:", oversatt_text)
