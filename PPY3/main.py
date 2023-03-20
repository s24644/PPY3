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

#=-------------Zadanie 3-----------------------------
print("=-=-=-=-=Zadanie 3=-=-=-=-=-=-")

rounds = input("podaj liczbe rund")
rounds = int(rounds)

game_type = input("podaj tryb gry (komputer/2 graczy)")

options_list = ["papier", "kamien", "nozyce"]

if(game_type == "komputer"):
    for i in range(0, rounds):
        player_weapon = input("Podaj swoja broń: ")
        randomVal = random.randint(0,2)
        computer_weapon = options_list[randomVal]
        print("Bron przeciwnika: ", computer_weapon)

        if player_weapon == "papier" and computer_weapon == "papier":
            print("remis")
        elif player_weapon == "papier" and computer_weapon == "kamien":
            print("Wygrywasz, gratulacje")
        elif player_weapon == "papier" and computer_weapon == "nozyce":
            print("Niestety przegrywasz")
        elif player_weapon == "kamien" and computer_weapon == "papier":
            print("Niestety przegrywasz")
        elif player_weapon == "kamien" and computer_weapon == "kamien":
            print("remis")
        elif player_weapon == "kamien" and computer_weapon == "nozyce":
            print("Wygrywasz, gratulacje")
        elif player_weapon == "nozyce" and computer_weapon == "papier":
            print("Wygrywasz, gratulacje")
        elif player_weapon == "nozyce" and computer_weapon == "kamien":
            print("Niestety przegrywasz")
        elif player_weapon == "nozyce" and computer_weapon == "nozyce":
            print("remis")



