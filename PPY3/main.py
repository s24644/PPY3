import sys


#-------------zadanie 1-------------------------------

liczby = input("podaj liczby oddzielone przecinkiem")

liczby = liczby.split(',')

max = int(liczby[0])
min = int(liczby[0])

for i in liczby:
    integerVal = int(i)
    if integerVal > max:
        max = integerVal
    if integerVal < min:
        min = integerVal

print(max)
print(min)

#--------------zadanie 2---------------------------


