num1 = int(input("number1: "))
num2 = int(input("number2: "))
way = input("Please choose an operation (+, -, *, /): ")

if way == "+":
    print(num1 + num2)
elif way == "-":
    print(num1 - num2)
elif way == "*":
    print(num1 * num2)
elif way == "/":
    if num2 != 0:  # Prevent division by zero
        print(num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")