import sys
import random

#-------------zadanie 1-------------------------------
print("=-=-=-=-Zadanie 1=-=-=-=-=")

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

print("Max:", max)
print("Min: ", min)

#--------------zadanie 2---------------------------
print("-=-=-=-Zadanie 2-=-=-=-=")

moja_lista = ["Warszawa", "Kraków", "Wrocław", "Łódź",
              "Poznań","Gdańsk", "Szczecin",
              "Bydgoszcz", "Lublin", "Białystok"]

counter = len(moja_lista)-1

for i in range(0,len(moja_lista)):
    random_index = random.randint(0,counter)
    print(moja_lista[random_index])
    moja_lista.pop(random_index)
    counter = counter - 1
