firstNumber = float(input("Enter first number: "))
secondNumber = float(input("Enter second number: "))
operation = input("Enter your operation e.g (+, -, *, /): ")

if operation == '+':
    print(firstNumber + secondNumber)
elif operation == '-':
    print(firstNumber - secondNumber)
elif operation == '*':
    print(firstNumber * secondNumber)
elif operation == '/':
    if secondNumber == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(firstNumber / secondNumber)
else:
    print("Operation not currently supported")
