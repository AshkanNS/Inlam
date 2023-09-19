#program som läser in ett antal temperaturer som uppmätts vid samma tidpunkt på olika platser.
#ska skriva ut medelvärdet av alla angivna temperaturer sedan skriva ut alla temperaturer som är högre än medelvärdet.
#de angivna temperaturerna ska vara numrerade från 1 och uppåt som mätstation 1 osv.

temperaturer = []   #vår lista för att lagra de angivna temperaturerna
nummer = 1          #nummerordning för våra mätstationer
# Loopar så att man kan ange temperaturerna
while True:
    temperatur_str = input(f"Ange temperatur för mätstation {nummer} (eller 'sluta' för att avsluta): ")
    
    if temperatur_str.lower() == 'sluta':
        break
    try:
        temperatur = float(temperatur_str)
        temperaturer.append(temperatur)
        nummer += 1
    except ValueError:
        print("Ogiltig inmatning. Ange en giltig temperatur eller 'sluta' för att avsluta.")

print("Angivna temperaturer:")  # Skriver ut de angivna temperaturerna med mätstationerna
for station, temperatur in enumerate(temperaturer, start=1):
    print(f"Mätstation {station}: {temperatur}°C")

medelvarde = sum(temperaturer) / len(temperaturer)  # Beräknar medelvärdet av temperaturerna

print(f"Medelvärde av temperaturerna: {medelvarde:.2f}°C")
print("Temperaturer högre än medelvärdet:")
for station, temperatur in enumerate(temperaturer, start=1):
    if temperatur > medelvarde:
        print(f"Mätstation {station}: {temperatur}°C")
