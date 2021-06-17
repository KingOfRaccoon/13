with open("24.txt") as file:
    data = file.read().split('Z')
    data.sort(key=lambda x: len(x))
    print(data[-1])
    print(len(data[-1]))
