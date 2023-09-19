#programmet jämför två texter för att se om de är anagram

text1 = input("Ange den första texten: ")
text2 = input("Ange den andra texten: ")

# Ta bort mellanslag och konvertera texterna till små bokstäver för att jämföra enklare
text1 = text1.replace(" ", "").lower()
text2 = text2.replace(" ", "").lower()

# Sortera båda texterna alfabetiskt
text1_sorted = sorted(text1)
text2_sorted = sorted(text2)

# Jämför de sorterade texterna för att se om de är anagram
if text1_sorted == text2_sorted:
    print("Ja, de är anagram av varandra.")
else:
    print("Nej, de är inte anagram av varandra.")
