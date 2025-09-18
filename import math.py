import math
x = int(input("Введіть трицифрове число: "))
a = x // 100
b = (x // 10) % 10
c = x % 10
if (a > b and a < c) or (a < b and a > c):
    mid = a
elif (b > a and b < c) or (b < a and b > c):
    mid = b
else:
    mid = c
print("Середня цифра:", mid)
print("Квадрат = {0} Куб = {1}".format(pow(mid, 2), pow(mid, 3)))