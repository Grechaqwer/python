# class Mashina:
#     def __init__(self, wheel:int, doors:int, pdk:bool):
#         self.wheels = wheel
#         self.doors = doors
#         self.pdk = pdk
#         self.probeg = 350000
#     def go_out(self):
#         if self.pdk == True:
#             self.pdk = False
#             return "Дядя Коля изгнан"
#         else:
#             return "Машина чиста. Его сдесь не было."
#
#         nissan = Mashina(pdk=False, wheel=8, doors=8)
#         # print(nissan.go_out())
#
#         print(nissan.pdk)
#         nissan.pdk = True
#
#         # print(nissan.__probeg) # private Нельзя ыводить
#         # nissan.__probeg = 500 # private(public) можно менять ??
#         nissan.__
# class Alphabet:
#     def __init__(self, lang, letters):
#         self.lang = lang
#         self.letters = letters
#     def print(self):
#         return  self.letters
#     def nums_kolvo(self):
#         return  len()
# alpha = Alphabet("eng", "abcdefghijklmnopqrstuvwxyz")
#     print(alpha.print())
#     print(alpha.nums_kolvo())

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("эта машинка стартует")

    def stop(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year

    def set_type(self, type):
        self.type = type

    def set_color(self, color):
        self.color = color
Antontop = Car("")