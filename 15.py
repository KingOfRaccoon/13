def getBin(num: int):
    return bin(num)[2:]

def xor(first: str, second: str):
    dif = len(first) - len(second)
    if dif > 0:
        for i in range(dif):
            second = '0' + second
    elif dif < 0:
        for i in range(abs(dif)):
            first = '0' + first
    ans = []
    for i in range(len(first)):
        ans.append(int(first[i])*int(second[i]))
    return len(set(ans)) == 1 and list(set(ans))[0] == 0

for a in range(101):
    check = True
    for x in range(1001):
        check = xor(getBin(x), getBin(39)) or (not xor(getBin(x), getBin(11))) or (not xor(getBin(x), getBin(a)))
        if check == False:
            break
    if check:
        print(a)

