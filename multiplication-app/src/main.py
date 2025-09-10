def multiply_two_digits(num1, num2):
    return num1 * num2

def is_valid_input(value):
    if value.isdigit() and 10 <= int(value) <= 99:
        return True
    return False

def main():
    print("Welcome to the Two-Digit Multiplication App!")
    
    num1 = input("Enter the first two-digit number: ")
    while not is_valid_input(num1):
        print("Invalid input. Please enter a two-digit number.")
        num1 = input("Enter the first two-digit number: ")
    
    num2 = input("Enter the second two-digit number: ")
    while not is_valid_input(num2):
        print("Invalid input. Please enter a two-digit number.")
        num2 = input("Enter the second two-digit number: ")
    
    result = multiply_two_digits(int(num1), int(num2))
    print(f"The result of multiplying {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()