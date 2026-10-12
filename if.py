
a = 100
b = 200
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")    

x= float(input("Enter a number: "))
operator = input("Enter an operator (+, -, *, /): ")
y = float(input("Enter another number: "))
if operator == "+":
    print("The sum is: ", x + y)
elif operator == "-":
    print("The difference is: ", x - y)
elif operator == "*":
    print("The product is: ", x * y)
elif operator == "/":
    print("The quotient is: ", x / y)
else:
    print("Invalid operator")