import random

def generator(length):
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '0123456789'
    symbols = '!@#$%^&*()-=+[]{}<>?/'
    
    all_characters = uppercase_letters + lowercase_letters + digits + symbols
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password


def password_generate():
    print("Password Generator")
    length = int(input("Enter the password length: "))
    
    if length < 5:
        print("Password length should be at least 6.")
    else:
        password = generator(length)
        print(f"Generated Password: {password}")


if __name__ == "__main__":
    password_generate()
