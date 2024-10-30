def input_numbers():
    numbers = []
    print("Введите числа. Введите 'стоп' для завершения ввода.")
    
    while True:
        user_input = input("Введите число: ")
        
        if user_input.lower() == 'стоп':
            break
        
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Введите действительное число или 'стоп' для выхода.")
    
    return numbers
def add(numbers):
    return sum(numbers)

def subtract(numbers):
    return numbers[0] - sum(numbers[1:])

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def integer_divide(numbers):
    result = int(numbers[0])
    for num in numbers[1:]:
        result //= int(num)
    return result

def exponentiate(base, exponent):
    return base ** exponent

def modulus(numbers):
    result = int(numbers[0])
    for num in numbers[1:]:
        result %= int(num)
    return result

def compare_two_numbers(a, b):
    if a > b:
        return f"{a} больше {b}"
    elif a < b:
        return f"{a} меньше {b}"
    else:
        return f"{a} равно {b}"

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    def find_min_max(numbers):
        return min(numbers), max(numbers)

def main():
    numbers = input_numbers()
    
    if len(numbers) < 2:
        print("Не хватает чисел для выполнения операций.")
        return
    
# Выполнение операций
    print(f"Сложение: {add(numbers)}")
    print(f"Вычитание: {subtract(numbers)}")
    print(f"Умножение: {multiply(numbers)}")
    try:
        print(f"Целочисленное деление: {integer_divide(numbers)}")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль.")
    print(f"Возведение в степень (первое число в квадрат): {exponentiate(numbers[0], 2)}")
    print(f"Остаток от деления: {modulus(numbers)}")

# Проверка на простое число
    num_to_check = int(input("Введите число для проверки на простоту: "))
    if is_prime(num_to_check):
        print(f"{num_to_check} - простое число.")
    else:
        print(f"{num_to_check} - составное число.")

if __name__ == "__main__":
    main()