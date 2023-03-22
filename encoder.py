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
            num -= 10
        password += str(num)
    return password


def decode(password):
    oldPass = ''
    for x in password:
        num = int(x)
        if num == 0:
            num = 7
        elif num == 1:
            num = 8
        elif num == 2:
            num = 9
        else:
            num = num - 3
        oldPass += str(num)
    return oldPass


# Have main and encode
def main():
    newPass = ''
    while True:
        menu()
        choice = int(input("Please enter an option:"))
        if choice == 1:
            digit = (input("Please enter your password to encode:"))
            newPass = encode(digit)
            print("Your password has been stored and encoded!")
        elif choice == 2:
            print(f"The encoded password is {newPass} and the original password is " + decode(newPass))
        elif choice == 3:
            break
        else:
            pass


if __name__ == '__main__':
    main()
