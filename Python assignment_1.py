# Basic Calculator Program

# Prompting the user for input (user to input first & second number)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the mathematical operation (+, -, *, /): ")

# Performing the operation 
if operation == '+':         #Addition
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':      #Substraction
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':      #Multiplication
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':       #Division
    if num2 != 0:  # Check to avoid division by zero
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Division by zero is not allowed!")
else:
    print("Invalid operation entered!")  

# End of the program