# import turtle
#
# screen = turtle.Screen()
# t = turtle.Turtle()
#
# side = int(input("Введи кол-во сторон: "))
# x = 80
# t.pensize(7)
# colors = ["red", "orange", "yellow", "green", "light blue"]
# for i in range(0, side):
#     t.fd(x) # forward
#     t.rt(360 / side) # rt = right
# screen.exitonclick()
# for
# lst = ["Антон", "Вова", "Гриша", "Олег", "Ян"]
# for element in lst: # для каждого элемента lst
#     print(element)
#
#
# for i in range(0, 10):
#      print(i)
#
# while
# is_game = True
# while is_game:
#     i = input("да/нет")
#     if i == "нет":
#         is_game = False
#
#     print("sue")
# word = input("Введите элю")
# while word:
#     print(word, end="")
#     word = word[:-1]
# z = int(input("Введите элю:"))
# while z:
#     z -= 1
#     if z % 2 == 0:
#         print(z,end=" ")
# x = int(input("Введите число: "))
# step = 0
# while x != 1:
#     step = step + 1
#     if x % 2 == 0:
#         x = x // 2
#         print(f"{step})", end =" ")
#         print(x, "/ 2 =", end=" ")
#         print(x)
#     else:
#         print(f"{step})", end=" ")
#         print(x, "* 3 + 1 =", end=" ")
#         x = 3 * x + 1
#         print(x)
# print("Шагов:", step)
import random
cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
is_game == "y"
while is_game:
    computer = [random.choice(cards)]
    player = [random.choice(cards)]
    score = 0
    get_card = "y"
    while get_card =="y":
        player.append(random.choice(cards)) # append - добавить в список
        if sum(player) > 21 and 11 in player:
            """если туз в руке и сумма 21"""
            for i in range(0,len(player)):
                if player [i] == 11:
                    player[i] = 1
                    break
        score = sum(player)
        print(f"Твоя рука: {player}. Очков: {score}")
        print("Первая карта компьютера:", computer [0])
        if score > 21:
            get_card = "n"
        else:
            get_card = input("y - взять карту,n - остановиться: ")

            while sum(computer) < 17:
                computer.append (random.choice(cards)))
                if sum(computer) > 21 and 11 in computer:
                    """если туз в руке и сумма 21"""
                for i in range(0, len(computer)):
                    if computer[i] == 11: \
                         computer[i] = 1
                          break
                score_compyter = sum(compyter)
                print("=" * 10)
                print(f"Твоя игровая рука: {player}.")
                print()



