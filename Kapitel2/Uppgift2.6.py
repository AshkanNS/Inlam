#ange hur många sekunder som ska räknas
sekunder = int(input("Ange sekunder: "))

timmar = sekunder // 3600       #division för resultat i heltal
restsekunder = sekunder % 3600  #restvärde av divisonen 
minuter = restsekunder // 60    #
sekunder = restsekunder % 60

print (f"Det har det gått: {timmar} timmar, {minuter} minuter, {sekunder}sekunder")