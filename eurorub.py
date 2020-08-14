print ("Конвертер валюты. \nЕвро в рубли. Рубли в евро.\n============================\n")
# задаем значения евро и рубля.
# 1 евро в рублях
eur=85.79
# курс  ЦБ РФ, на 11.08.2020
# 1 рубль в евро
rub=0.0124
# перевод евро в рубли
etor=float(input("EUR в RUB, введите число: ",))
rese=round((etor*eur),4)
print('EUR =', float(etor))
print("RUB =",float(rese))
print("")
# перевод рублей в евро
rtoe=float(input("RUB в EUR, введите число: ",))
resr=round ((rtoe*rub),4)
print("RUB =",float(rtoe))
print("EUR =",float(resr))   

