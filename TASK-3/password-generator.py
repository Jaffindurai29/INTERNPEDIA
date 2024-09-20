import secrets
import string
import pyperclip

def welcome_message():
    print("Welcome to the Secure Password Generator!")
    print("You can generate passwords with different complexities.")
    print("Specify the length and choose the character sets.\n")

def get_password_requirements():
    while True:
        try:
            length = int(input("Enter password length: "))
            if length < 1:
                print("Password length must be a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        print("Include in password:")
        include_upper = input("Uppercase letters? (y/n): ").lower() == 'y'
        include_lower = input("Lowercase letters? (y/n): ").lower() == 'y'
        include_digits = input("Digits? (y/n): ").lower() == 'y'
        include_symbols = input("Symbols? (y/n): ").lower() == 'y'
        
        if not (include_upper or include_lower or include_digits or include_symbols):
            print("You must include at least one character set. Try again.")
        else:
            return length, include_upper, include_lower, include_digits, include_symbols

def generate_password(length, include_upper, include_lower, include_digits, include_symbols):
    char_pool = ''
    
    if include_upper:
        char_pool += string.ascii_uppercase
    if include_lower:
        char_pool += string.ascii_lowercase
    if include_digits:
        char_pool += string.digits
    if include_symbols:
        char_pool += string.punctuation
    
    password = ''.join(secrets.choice(char_pool) for _ in range(length))
    return password

def generate_multiple_passwords():
    while True:
        num_passwords = input("\nHow many passwords would you like to generate? ")
        try:
            num_passwords = int(num_passwords)
            if num_passwords < 1:
                print("Please enter a positive number.")
                continue
            return num_passwords
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def copy_to_clipboard(password):
    copy_option = input("Would you like to copy the password to the clipboard? (y/n): ").lower()
    if copy_option == 'y':
        pyperclip.copy(password)
        print("Password copied to clipboard!")

def password_generator():
    welcome_message()
    
    length, include_upper, include_lower, include_digits, include_symbols = get_password_requirements()
    num_passwords = generate_multiple_passwords()

    for i in range(1, num_passwords + 1):
        password = generate_password(length, include_upper, include_lower, include_digits, include_symbols)
        print(f"Password {i}: {password}")
        copy_to_clipboard(password)
    
    print("\nThank you for using the Secure Password Generator!")

if __name__ == "__main__":
    password_generator()
