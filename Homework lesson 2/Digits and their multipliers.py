number = input('Введите число, я разложу его на разряды и множетели ')
a = list(str(number))
print('множетели числа ' + number )
print(a)
b = []
number1 = int(number)
stepen = 0
while number1 > 1:
    number1 = number1 /10
    stepen = stepen + 1
    b.append(stepen)
b.append(0)
set(b)
b.sort(reverse = True)
print('степени числа ' + number)
print(b)

