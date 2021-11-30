zapros = int(input('В ведите сумму снятия '))
snatie = 0
ostsnatie = zapros
sumSnat500 = 0
sumSnat200 = 0
sumSnat100 = 0
sumSnat50 = 0
if ostsnatie >= 500:
    sumSnat500 = ostsnatie // 500
    snatie = sumSnat500 * 500
    ostsnatie = ostsnatie - snatie
if ostsnatie >= 200:
    sumSnat200 = ostsnatie // 200
    snatie = sumSnat200 * 200
    ostsnatie = ostsnatie - snatie
if ostsnatie >= 100:
    sumSnat100 = ostsnatie // 100
    snatie = sumSnat100 * 100
    ostsnatie = ostsnatie - snatie
if ostsnatie >= 50:
    sumSnat50 = ostsnatie // 50
    snatie = sumSnat50 * 50
    ostsnatie = ostsnatie - snatie
if ostsnatie < 50:
    print("Банкомат выдал следующие купюры " + str(sumSnat500) + " по 500, " + str(sumSnat200) + " по 200, "
    + str(sumSnat100) + " по 100, " + str(sumSnat50) + " по 50, " + "остаток не снимаемой суммы " + str(ostsnatie))