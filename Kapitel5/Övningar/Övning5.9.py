#kontrollerar om angivet personnr är korrekt/giltigt

personnr = input('Skriv ditt personnr (yymmdd-xxxx): ')
personnr_str = personnr.replace(' ', '').replace('-', '')   #tar bort all mellanslag och - tecken från texten

# Kontrollerar om personnumret har rätt längd (10 tecken)
if len(personnr_str) != 10:
  print('Ogiltigt personnummer, måste vara 10 siffror.')
else:
  
  try:
    digits = [int(digit) for digit in personnr_str] # Konverterar varje siffra i personnumret till en lista av heltal
    result = []                                     # resultatet av beräkningen
    for i, num in enumerate(digits[:-1]): # Loopa igenom siffrorna i personnumret, med start från första siffran
      if i % 2 == 0: 
        double_digit = num * 2
        if double_digit > 9:
          result.append(double_digit - 9)  
        else:
          result.append(double_digit)
      else:
        result.append(num)
        
    total = (sum(result) + digits[-1])  # Beräknar den totala summan av siffrorna i resultatet och den sista siffran
    
    if total % 10 == 0:     # Kontrollera om den totala summan är jämnt delbar med 10
      print('Korrekt personnummer')
    else:
      print('Ogiltigt personnummer')
      
  except ValueError:
    print('Ogiltigt personnummer. Ange enbart siffror och bindestreck.')