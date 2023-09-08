
#ränteberäkning

ränta = float(input("räntesats? "))
n = int(input("antal år? "))
kapital = 1000

for år in range(1, n+1, 1):
    kapital = kapital + kapital * 0.01 * ränta
    print (f"{år:2}{kapital:5.0f}")