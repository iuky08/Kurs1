import random

def main():
    # Случайным образом выбираем число от 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 5

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. У тебя есть 5 попыток, чтобы угадать его.")

    for attempt in range(1, attempts + 1):
        while True:
            try:
                guess = int(input(f"Попытка {attempt}: Введите ваше предположение: "))
                break
            except ValueError:
                print("Пожалуйста, введите целое число.")

        if guess < secret_number:
            print("Слишком маленькое число.")
        elif guess > secret_number:
            print("Слишком большое число.")
        else:
            print(f"Поздравляю! Ты угадал число {secret_number} с {attempt}-й попытки!")
            break
    else:
        print(f"К сожалению, ты не угадал число. Загаданное число было {secret_number}.")

if __name__ == "__main__":
    main()