#program som läser in rövarspråk och översätter till svenska, använd övning5.4 för att fylla i text

# Läs in texten i rövarspråk från användaren
rovarsprak_text = input('Skriv i rövarspråk: ')
oversatt_text = ""
i = 0

# Loopa igenom varje tecken i rövarspråkstexten
while i < len(rovarsprak_text):
    if rovarsprak_text[i].lower() in 'bcdfghjklmnpqrstvwxyz':   # Kolla om det aktuella tecknet är en konsonant i rövarspråk (har en "o" efter sig)
        oversatt_text += rovarsprak_text[i] # Om det är en konsonant, lägg till det i den översatta texten
        i += 3                              # Hoppa över nästa två tecken ('o' och konsonant) i rövarspråket
    else:
        oversatt_text += rovarsprak_text[i]  # Om det inte är en konsonant (vokal eller annat tecken), lägg till det i den översatta texten
        i += 1

# Skriv ut den översatta texten till vanlig svenska
print(f'Rövarspråket: {rovarsprak_text}\nÖversatt: {oversatt_text}')
