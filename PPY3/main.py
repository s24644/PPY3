import sys


#-------------zadanie 1-------------------------------

liczby = input("podaj liczby oddzielone przecinkiem")

liczby = liczby.split(',')

max = -1
min = sys.maxsize

for i in liczby:
    integerVal = int(i)
    if integerVal > max:
        max = integerVal
    if integerVal < min:
        min = integerVal

print(max)
print(min)
