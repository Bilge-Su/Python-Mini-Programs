def calculate(a, b, operation):
    if operation not in "+-*/":
        return "Please choose one these operation signs: +-*/"
    if operation == "+":
        return (str(a) + " + " + str(b) + " = " + str(a+b))
    if operation == "-":
        return (str(a) + " - " + str(b) + " = " + str(a-b))
    if operation == "*":
        return (str(a) + " * " + str(b) + " = " + str(a*b))
    if operation == "/":
        return (str(a) + " / " + str(b) + " = " + str(a/b))

while True:
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        operation = input("Enter the operation: +-*/")
        print(calculate(a, b, operation))
    except:
        print("Please enter a number.")