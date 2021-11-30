fizz = int(input('Введите первое число '))
buzz = int(input('Введите второе число '))
number3 = int(input('Введите третье число '))
a = []
i = 0
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

