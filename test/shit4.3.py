
#def god (tal):
#    if tal < 0:
#       utdata = "minsta"
#   elif tal > "största":
#       utdata = "största"
#   else: 
#       tal < "minsta"
#   return utdata
#
# b = float(input("Skriv tal: "))
# print (god(b))


def hitta_storsta_minsta():
    storsta = float('-inf')  # Använd negativt oändligt som startvärde för största
    minsta = float('inf')    # Använd positivt oändligt som startvärde för minsta

    while True:
        tal = float(input("Skriv ett tal (negativt tal för att avsluta): "))
        if tal < 0:
            break
        if tal > storsta:
            storsta = tal
        if tal < minsta:
            minsta = tal

    return storsta, minsta

största, minsta = hitta_storsta_minsta()
print(f"Största Talet: {största}")
print(f"Minsta talet: {minsta}")

    