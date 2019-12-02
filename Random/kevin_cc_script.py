def is_valid_card(card_number, card_number_length):
    if card_number_length in {13, 15, 16} and card_number.isdigit():
        return True
    return False


def sum_check(card_number):
    card_number_list = list(map(int, card_number))
    arithmetic_comprehension = [((num * 2)//10 + (num * 2 % 10))
                                for num in card_number_list[-2::-2]]
    total_sum = sum(arithmetic_comprehension + card_number_list[-1::-2])
    if total_sum % 10 == 0:
        return True
    return False


def card_type_check(card_number, card_number_length):
    if (card_number_length == 13 or card_number_length == 16) and card_number.startswith('4'):
        return"VISA"
    elif card_number_length == 15 and card_number.startswith(('34', '37')):
        return "AMEX"
    elif card_number_length == 16 and card_number.startswith(('51', '52', '53', '54', '55')):
        return "MASTERCARD"
    return "Your card number is invalid."


def main():
    while True:
        card_number = input(
            "Enter in a valid credit card number. Type lata to exit. ")
        card_number_length = len(card_number)
        if card_number.lower() == 'lata':
            print("Goodbye.")
            break
        if not is_valid_card(card_number, card_number_length) or not sum_check(card_number):
            print("Card number is invalid.")
            continue
        print(card_type_check(card_number, card_number_length))
        print("Program End.")
        break


if __name__ == '__main__':
    main()
