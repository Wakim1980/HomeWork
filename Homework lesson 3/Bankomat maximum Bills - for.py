summsnat = int(input('Сколько вы хотите снять денег  '))
List_ = [500 , 200 , 100 , 50 ]
itog = []
itogDan = []
kup =[]
for element in List_:
    itog = summsnat // element
    summsnat = summsnat - (itog * element)
    itogDan.append(element)
    kup.append(itog)
print(str(itogDan) + ' номиналы купюр')
print(str(kup) + ' количество купюр')
if summsnat < 50:
    print('Остаток суммы снятия ' + str(summsnat))