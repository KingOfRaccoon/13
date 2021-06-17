num = 5 * 36**7 + 6**10 - 36
string = ""
while num > 0:
    string += str(num % 6)
    num = num // 6
print(string)
print(string.count('5'))