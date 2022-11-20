import random
import datetime

while True:
    number = input("Сколько дней рождения мы генерирем ? (до 65)")
    if not number.isdigit() or int(number) > 65 or int(number) < 2:
        print("Это по-твоему смешно? Нормально введи,пожалуйста")
    else:
        number = int(number)
        break

birthdays = []
star = datetime.date(2022, 1, 1)
for _ in range(number):
    randomNumberOfDays = datetime.timedelta(random.randint(0,364))
    birthday = star + randomNumberOfDays
    birthdays.append(birthday)

for i in range(number):
    print(f"{i + 1}) {birthdays[i]}")

print("=" * 10)
for i in set(birthdays):
    if birthdays.count(i) > 1:
        print(f"- {i.strftime('%d.%m.%y')} встречается {birthdays.count(i)} раза.")

