from math import isqrt

def getDels(num: int):
    dels = []
    for i in range(2, isqrt(num)+1):
        if num % i == 0 and num % 2 == 0:
            dels.append(i)
    obr_dels = []
    for i in dels:
        if (num//i) % 2 == 0:
            obr_dels.append(num//i)
    for i in obr_dels: dels.append(i)
    if num % 2 == 0: dels.append(num)
    return sorted(list(set(dels)))

for i in range(92632, 92700 + 1):
    dels = getDels(i)
    if len(dels) == 6:
        print(dels)