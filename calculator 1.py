# Display the Calculator Mwnu
print("Welcome to the Calculator!")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

#Get the user's choice

choice = input("Please select an operation (1-5): ")
#Get the numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
#Perform the selected operation
if choice == '1':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif choice == '2':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")
elif choice == '3':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
elif choice == '5':
    result = num1 % num2
    print(f"The result of {num1} % {num2} is: {result}")
else:
    print("Invalid operation selected. Please choose a number between 1 and 5.")
    