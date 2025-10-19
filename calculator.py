def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def exponent(x, y):
    return x ** y

def modulus(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x % y

def floor_divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x // y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to Basic Calculator")

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponent")
        print("6. Modulus")
        print("7. Floor Division")
        print("8. Exit")
        
        choice = input("Enter choice (1-8): ")
        
        if choice == '8':
            print("Exiting... Goodbye!")
            break
        
        if choice not in [str(i) for i in range(1,8)]:
            print("Invalid Input. Please enter a number between 1 and 8.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", exponent(num1, num2))
        elif choice == '6':
            print("Result:", modulus(num1, num2))
        elif choice == '7':
            print("Result:", floor_divide(num1, num2))

if __name__ == "__main__":
    main()
