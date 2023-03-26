min_length = 4  # minimum length required for the password


def main():
    password = get_password(min_length)
    print(password)

def get_password(min_length):
    global password

    password = input(f"Enter a password with at least {min_length} characters: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter a password: ")
    print("Password set successfully!")
    print("Your password is:", "*" * len(password))


get_password(min_length)

main()
