# калькулятор
num1 = int(input("введите первое целое число: "))
num2 = int(input("введите второе целое число: "))
operation = input("введите математическую операцию (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("деление на ноль невозможно")
    else:
        result = num1 / num2
else:
    print("неверная операция")

if operation in "+-*/":
    print("результат:", result)
