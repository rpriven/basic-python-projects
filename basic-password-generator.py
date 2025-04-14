import random
import string

def generate_password(length=12):
    """Generate a simple random password of specified length."""
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = '!@#$%^&*()-_=+'
    
    # Combine all characters
    all_chars = lowercase + uppercase + digits + special
    
    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Simple command line interface
if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length (default is 12): ") or "12")
        password = generate_password(length)
        print(f"Your generated password is: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")
