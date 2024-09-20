def welcome_message():
    print("Welcome to the Simple Calculator!")
    print("You can perform addition, subtraction, multiplication, and division.")
    print("Type 'exit' at any time to quit the program.\n")

def farewell_message():
    print("\nThank you for using the calculator. Goodbye!")

def get_operation():
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    return input("Enter the operation (+, -, *, /): ")

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numerical values.")

def perform_calculation(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Error! Division by zero is not allowed."

def calculator():
    while True:
        operation = get_operation()
        
        if operation == 'exit':
            break
        
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please try again.")
            continue
        
        num1, num2 = get_numbers()
        result = perform_calculation(operation, num1, num2)
        
        print(f"Result: {result}")
    
def main():
    welcome_message()
    calculator()
    farewell_message()

if __name__ == "__main__":
    main()
