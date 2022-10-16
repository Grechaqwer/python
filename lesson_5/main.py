x = 7
# if - если
# eise - иначе
if x <= 10 or x == 15:  # икс меньше или равно десяти
    print("Икс не больше 10")
else:
    print("Икс больше 10")
    x = 10
    # x = 10
    # print(x == 10) # правда = True
    # print(x == 5) # ложь =  False

    # x = int(input("Введите число: "))
    # if x < 0:
    #     print("Отрицательное")
    # elif x > 0: # elif - else if = иначе если
    #     print("Положительное")
    # else :
    #     print("Нолик")
    year = int(input("Введите число: "))

    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
          print("Високосненько")
    else:
        print("Не високосненько :")
        number_1 = int
