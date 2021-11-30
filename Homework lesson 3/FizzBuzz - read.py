filenamein = 'fizzbuzz.txt'
fileRead = open(filenamein, 'r')
a = []
i = 0
for line in fileRead:
    fizz, buzz, number3 = line.split()
    fizz = int(fizz)
    buzz = int(buzz)
    number3 = int(number3)
    while i < number3:
        i = i + 1
        if i % fizz == 0 and i % buzz == 0:
            a.append('FB')
        elif i % fizz == 0:
            a.append('F')
        elif i % buzz == 0:
            a.append('B')
        else:
            a.append(i)
    print(a)
fileRead.close()