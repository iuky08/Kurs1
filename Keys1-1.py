def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

def main():
    while True:
        user_input = input("Введите положительное целое число: ")
        try:
            number = int(user_input)
            if number < 0:
                print("Пожалуйста, введите положительное число.")
            else:
                result = calculate_factorial(number)
                print(f"Факториал числа {number} равен {result}")
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()