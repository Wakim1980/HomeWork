file1 = 'fizzbuzz.txt'
file2 = 'void.txt'
f1 = open(file1, 'r')
f2 = open(file2, 'w')
i = 0
for Lane in f1:
    for line in f1:
        fizz, buzz, number3 = line.split()
        fizz = int(fizz)
        buzz = int(buzz)
        number3 = int(number3)
        while i < number3:
            i = i + 1
            if i % fizz == 0 and i % buzz == 0:
                f2.write('FB')
            elif i % fizz == 0:
                f2.write('F')
            elif i % buzz == 0:
                f2.write('B')
            else:
                f2.write(str(i))
f1.close()
f2.close()