#program som läser in längd bredd och tjocklek o undersöker om breven har 
#tillåtna mått eller inte

längd = int(input("Ange brevets längd: "))
bredd = int(input("Ange brevets bredd: "))
tjocklek = int(input("Ange brevets tjocklek: "))

if (140 <= längd <= 600) and (90 <= bredd+längd+tjocklek <= 900) and ( tjocklek <= 100):
    print ("Vi har noterat dina mått")
else:
    print ("Du har överskridit måtten")
