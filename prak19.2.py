import pandas as pd
from numpy import *

f = open("text_ukr.txt", 'r', encoding="utf-8")
all_words = []

for line in f:
    parts = line.split()
    for w in parts:
        all_words.append(w)

f.close()

s = pd.Series(all_words)

print("Усі слова у Series:")
print(s)

vowels = "аеєиіїоуюя"

selected = []

for w in all_words:
    cnt = 0
    for ch in w.lower():
        if ch in vowels:
            cnt += 1
    if cnt >= 3:
        selected.append(w)

f2 = open("output.txt", "w", encoding="utf-8")
for w in selected:
    f2.write(w + "\n")
f2.close()

print("\nСлова з 3+ голосними записано у output.txt")
