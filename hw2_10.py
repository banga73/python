import random

N = int(input ("Введите число: "))
i = 0
k = 0
while i < N:
    temp = random.randint(0, 1)
    print(temp)
    i = i + 1
    if temp == 0:
        k = k + 1
if k < N // 2:
    print(k)
else:
    print(N - k)