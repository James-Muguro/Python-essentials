# ## Password Generator

import string

def generate_password(length=15):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    password_length = int(input("Enter the desired password length: "))

    if password_length < 5:
        print("Invalid password length. Please enter a number higher than 5.")
        return

    password = generate_password(password_length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()




