import math
x = int(input("Введіть двоцифрове число:"))
a = x // 10
b = x % 10
d = [a, b]
c = [i * 100 + j * 10 + k for i in d for j in d for k in d]
print("Квадрати чисел: ")
for n in c:
    print("{0}^2 = {1}".format(n,pow(n, 2)))
