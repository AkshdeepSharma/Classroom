def checkValidPassword(password, entered_password):
    if password == entered_password or entered_password.swapcase() == password:
        return "Yes"
    if entered_password in password:
        password = password.replace(entered_password, "")
        if len(password) == 1 and password.isdigit():
            return "Yes"
    return "No"


def main():
    password = input()
    entered_password = input()
    print(checkValidPassword(password, entered_password))


if __name__ == "__main__":
    main()
