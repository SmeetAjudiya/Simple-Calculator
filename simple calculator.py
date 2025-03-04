def addition(x , y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

print("CALCULATOR")

print("Select Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    choice = input("Enter choice(1,2,3,4): ")

    if choice in ('1', '2', '3', '4'):
        try:
            number1 = float(input("Enter First Number: "))
            number2 = float(input("Enter Second Number: "))
        except ValueError:
            print("Invalid Choice. Please enter a number")

        if choice == '1':
            print(number1, "+", number2, "=", addition(number1, number2))
    
        elif choice == '2':
            print(number1, "-", number2, "=", subtraction(number1, number2))

        elif choice == '3':
            print(number1, "*", number2, "=", multiplication(number1, number2))
    
        elif choice == '4':
            (number1, "/", number2, "=", division(number1, number2))

        next_calculation = input("Want to do another calculation? Yes/No: ")

        if next_calculation == 'no':
            print("Exiting Calcuator !!!")
            break
    else:
        print("Invalid Input")
