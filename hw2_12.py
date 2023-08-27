S = int(input ("Введите число: "))
P = int(input ("Введите число: "))
err = 0
for i in range(1, int(P / 2)):
    if P % i == 0 and i + P / i == S:
       print(i, int(P / i))
       err = 1
       break
if err == 0: print('No such numbers')