import math

def main():
    while True:
        user_input = input("Введите положительное целое число: ")
        try:
            number = int(user_input)
            if number < 0:
                print("Пожалуйста, введите положительное число.")
            else:
                result = math.factorial(number)
                print(f"Факториал числа {number} равен {result}")
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()