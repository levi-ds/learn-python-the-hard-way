operator = input("Enter an operator (+, -, *, /): ")

if operator not in ["+","-","*","/"]:
    print("Enter valid operator.")
else:
    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(round(num1 / num2,3))
    else:
        print("Enter a valid operator")