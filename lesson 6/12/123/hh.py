# a = int(input())
# b = int(input())
#
# for mega_anton in  range(a + 1,b):
#     lst.append(mega_anton ** 2)
# print(lst)
#
# text = input("Сообщение: ")
# lst =
# print(lst)
#
# text = input("Сообщение: ")
# lst = text.split(" ")
# print(lst)
# lst.reverse()
# print(lst)
number = input("Число: ")
while number != "end":
    number = input("Число: ")
    if number.isdigit():
        number = int(number)
    else:
        print("Введи число!")
        continue

    if number.lstrip("-").isdigit():
        number = int(number)
    else:
        print("Введи число!")
        continue

    if number % 2 == 0:
        сы