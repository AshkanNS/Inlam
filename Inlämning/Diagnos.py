
while True:
    n = int(input("Ange tal mellan 1-99: "))
    if n <=1 or n >= 99:
        print("Ange ett nr mellan  1-99")
    else:
        break
for i in range (2,n+1):
    for j in range (2,n+1):
        if i % j == 0:
          break
    if i == j:
        print (i, end=",")