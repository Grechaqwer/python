import random

life = 10
length = 3

answer = random.randint(100, 999)
answer = str(answer)

while life:
    is_guessed = False
    print("Жизней:", end="")
    for i in range(life):
        print("❤", end="")
    print()


    guess = input("Предположение: ")
    if len(guess) != length or not guess.isdigit():
        print("Число от 100 до 999")
        continue

    if guess == answer:
        print("Пабеда")
        is_guessed = True
        break
    if not is_guessed:

        for i in range(length):
            if guess[i] == answer[i]:
                print("Fermi")
                is_guessed = True
                break

    if not is_guessed:# если не отгодал
     # проверка на pico
        for char in guess:# для каждого символа в guess
            if char in answer: # если число в ответе
                print("PICO")
                is_guessed = True
                break

    if not is_guessed:
        print("Bagels")

    life -= 1



