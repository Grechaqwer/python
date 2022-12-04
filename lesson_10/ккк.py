# def hello_world():  # объявление функции
#     print("hello_world")
#
# # ----------------------
# hello_world()  # вызов функции

# def plus(chislo1:int, chislo2:int) -> int:  # type hinting
#     """Эта функция отвечает за сложение."""
#     answer = chislo1 + chislo2
#     return answer  # что вернет функция
#
# x = plus(54, 88)  # записали результат функции в переменную
# print(x + 2)

# def is_sorted(liist_0ne):
#     clone_l = sorted(liist_0ne)#cортерованный список
#     if liist_0ne == clone_l:
#         return True
#
#
# l = [1,5,6,7,8]
#
# if is_sorted(l): #ECли функция вернула true
#     print("сортEроваННо")
# else:
#     print("не сортEроваННо")


# 2 задача

# def find_longest( slova1 ):
#     shifri =[]
#     for i in slova1:
#         shifri.append(len(i)) # добавление элемента в список
#     ind228=shifri.index(max(shifri))
#     return slova1[ind228],shifri[ind228]
#
# slova =["tank","minecraft","egg","connect","H2o-sostav"]
#
# print(find_longest(slova))

# 3 задача

def min_max(qwe):
    mini = qwe[0]
    maxi = qwe[0]
    for i in qwe:
        if i > maxi:  # если найден новый максимум
            maxi = i  # перезапись максимума
        elif i < mini:
            mini = i
    return mini, maxi


qwe = [4, 3, 5, 6, 7]
print("Минимальное:", min_max(qwe)[0], "Максимальное:", min_max(qwe)[1])
# print("Минимальное:"min_max"Max"(qwe))
