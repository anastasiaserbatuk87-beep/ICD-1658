import pandas as pd
from numpy import *

df = pd.read_csv("input.csv", header=None)

sum1 = df[0].sum()
sum2 = df[1].sum()
sum3 = df[2].sum()

list1 = ["Фірма 1", "Фірма 2", "Фірма 3"]
list2 = [sum1, sum2, sum3]
list = [[], []]

list[0] = list1
list[1] = list2

result = pd.DataFrame(list)
result = result.T

print("Загальна кількість покришок кожної фірми:")
print(result)