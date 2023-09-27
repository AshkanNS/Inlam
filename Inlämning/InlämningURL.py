import requests             #modulen används för att integrerar med webbsidor enkelt

#vår function för översättning från svenska till rövarspråk
def rov_sprok (rs):
    konsonanter = "bcdfghjklmnpqrstvwxyzåäö"
    t = ""                          #en tom sträng för att lagra översättningen
    for i in (rs):
        if i in konsonanter:
            t += i + "o" + i
        else:
            t += i
    return t

fileurl = "https://github.com/AIDEV23S/svText/blob/main/svenskt_text.txt?raw=true"  #ange url till filen som ska hämtas
req = requests.get(fileurl)                                                         #försöker läsa filen genom angiven länk

if req.status_code == 200:          #kontrollerar om länken är korrekt/ leder till en verklig sajt
    file_content = req.text         #läser in innehållet i länken till filen
    print ("Angiven länk kommer att översättas till en ny fil!")
    file_name = input("Ange nya filens namn: ")                     #ange önskat namn till nya filen

    with open (file_name, "w", encoding="utf-8") as nyfil:          #här använder vi with sats för att garantera att alla filer också stängs vid avslut
        for rad in file_content.splitlines():                       #läser in varje rad i filens innehåll och delar upp raderna
            translate = rov_sprok(rad)                              #översätter raderna till rövarspråket med får tillagda funktion
            nyfil.write(translate + "\n")                           #skriver in allt i den nya filen

    print ("Fil översatt")  
else:
    print("Kunde inte hämta filen från URL:en", req.status_code)       #kontrollerar felkod ifall angiven länk skulle vara fel
