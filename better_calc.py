num1 = float (input("Enter first number: "))
op = (input("Enter math operator: "))
num2 = float (input("Enter second numer: "))


if op == "+":
    print(num1 + num2)
elif op == "-": 
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")

