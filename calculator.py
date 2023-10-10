# Оптимизированный способ
num1 = int(input("Введите первое целое число: "))
num2 = int(input("Введите второе целое число: "))
operation = input("Введите математическую операцию (+, -, *, /): ")

if operation in "+-*/":
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("На ноль делить нельзя!")
        else:
            result = num1 / num2
    print("Результат:", result)
else:
    print("Неверная операция")
