import getpass
import random

# -------------zadanie 1-------------------------------
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

# --------------zadanie 2---------------------------
print("-=-=-=-Zadanie 2-=-=-=-=")

moja_lista = ["Warszawa", "Kraków", "Wrocław", "Łódź",
              "Poznań", "Gdańsk", "Szczecin",
              "Bydgoszcz", "Lublin", "Białystok"]

counter = len(moja_lista) - 1

for i in range(0, len(moja_lista)):
    random_index = random.randint(0, counter)
    print(moja_lista[random_index])
    moja_lista.pop(random_index)
    counter = counter - 1

# =-------------Zadanie 3-----------------------------
print("=-=-=-=-=Zadanie 3=-=-=-=-=-=-")

rounds = input("podaj liczbe rund")
rounds = int(rounds)

game_type = input("podaj tryb gry (komputer/2 graczy)")

player1_name = input("Podaj nazwe pierwszego gracza: ")
player2_name = ""

options_list = ["papier", "kamien", "nozyce"]

round_list = []

player1_win_counter = 0
player2_win_counter = 0

if (game_type == "komputer"):
    player2_name = "Komputer"
    for i in range(0, rounds):
        player_weapon = input("Podaj swoja broń: ")
        randomVal = random.randint(0, 2)
        computer_weapon = options_list[randomVal]

        print("Bron przeciwnika: ", computer_weapon)

        if player_weapon == "papier" and computer_weapon == "papier":
            round_list.append("Remis")
        elif player_weapon == "papier" and computer_weapon == "kamien":
            round_list.append("Wygrywa " + player1_name)
            player1_win_counter += 1
        elif player_weapon == "papier" and computer_weapon == "nozyce":
            round_list.append("Wygrywa " + player2_name)
            player2_win_counter += 1
        elif player_weapon == "kamien" and computer_weapon == "papier":
            round_list.append("Wygrywa " + player2_name)
            player2_win_counter += 1
        elif player_weapon == "kamien" and computer_weapon == "kamien":
            round_list.append("remis")
        elif player_weapon == "kamien" and computer_weapon == "nozyce":
            round_list.append("Wygrywa " + player1_name)
            player1_win_counter += 1
        elif player_weapon == "nozyce" and computer_weapon == "papier":
            round_list.append("Wygrywa " + player1_name)
            player1_win_counter += 1
        elif player_weapon == "nozyce" and computer_weapon == "kamien":
            round_list.append("Wygrywa " + player2_name)
            player2_win_counter += 1
        elif player_weapon == "nozyce" and computer_weapon == "nozyce":
            round_list.append("remis")
elif game_type == "2 graczy":
    player2_name = input("Podaj nazwe drugiego gracza: ")
    for i in range(0, rounds):
        print("=-=-=-=-=-=RUNDA " + str(i+1) + "=-=-=-=-=-=")
        player1_weapon = getpass.getpass(player1_name + ", podaj swoją broń: ")
        player2_weapon = getpass.getpass(player2_name + ", podaj swoją broń: ")

        if player1_weapon == "papier" and player2_weapon == "papier":
            round_list.append("Remis")
            print("Bron gracza " + player1_name + ": " + player1_weapon)
            print("Bron gracza " + player2_name + ": " + player2_weapon)
        elif player1_weapon == "papier" and player2_weapon == "kamien":
            round_list.append("Wygrywa " + player1_name)
            player1_win_counter += 1
            print("Bron gracza " + player1_name + ": " + player1_weapon)
            print("Bron gracza " + player2_name + ": " + player2_weapon)
        elif player1_weapon == "papier" and player2_weapon == "nozyce":
            round_list.append("Wygrywa " + player2_name)
            player2_win_counter += 1
            print("Bron gracza " + player1_name + ": " + player1_weapon)
            print("Bron gracza " + player2_name + ": " + player2_weapon)
        elif player1_weapon == "kamien" and player2_weapon == "papier":
            round_list.append("Wygrywa " + player2_name)
            player2_win_counter += 1
            print("Bron gracza " + player1_name + ": " + player1_weapon)
            print("Bron gracza " + player2_name + ": " + player2_weapon)
        elif player1_weapon == "kamien" and player2_weapon == "kamien":
            round_list.append("remis")
            print("Bron gracza " + player1_name + ": " + player1_weapon)
            print("Bron gracza " + player2_name + ": " + player2_weapon)
        elif player1_weapon == "kamien" and player2_weapon == "nozyce":
            round_list.append("Wygrywa " + player1_name)
            player1_win_counter += 1
            print("Bron gracza " + player1_name + ": " + player1_weapon)
            print("Bron gracza " + player2_name + ": " + player2_weapon)
        elif player1_weapon == "nozyce" and player2_weapon == "papier":
            round_list.append("Wygrywa " + player1_name)
            player1_win_counter += 1
            print("Bron gracza " + player1_name + ": " + player1_weapon)
            print("Bron gracza " + player2_name + ": " + player2_weapon)
        elif player1_weapon == "nozyce" and player2_weapon == "kamien":
            round_list.append("Wygrywa " + player2_name)
            player2_win_counter += 1
            print("Bron gracza " + player1_name + ": " + player1_weapon)
            print("Bron gracza " + player2_name + ": " + player2_weapon)
        elif player1_weapon == "nozyce" and player2_weapon == "nozyce":
            round_list.append("remis")
            print("Bron gracza " + player1_name + ": " + player1_weapon)
            print("Bron gracza " + player2_name + ": " + player2_weapon)

print("=-=-=-=WYNIKI=-=-=-=-=")

for i in range(1, len(round_list) + 1):
    print("Runde " + str(i) + " wygrywa: " + round_list[i-1])

if player1_win_counter > player2_win_counter:
    print("Grę wygrywa: " + player1_name)
elif player2_win_counter > player1_win_counter:
    print("Grę wygrywa: " + player2_name)
else:
    print("Remis")





