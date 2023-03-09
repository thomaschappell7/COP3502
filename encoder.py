def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(digit):
    password = ' '
    for char in digit:
        num = int(char)
        num += 3
        if num > 9:
            num -=10
        password += str(num)
    return password

# Have main and encode
def main():
    while True:
        menu()
        choice = int(input("Please enter an option:"))
        if choice == 1:
            digit = (input("Please enter your password to encode:"))
            encode(digit)
            print("Your password has been stored and encoded!")
        elif choice == 3:
            break
        else:
            pass


if __name__ == '__main__':
    main()
