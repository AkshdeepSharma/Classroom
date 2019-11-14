def convert_miles_to_roman_paces(miles):
    roman_paces = round(miles * 1000 * (5280 / 4854))
    return roman_paces


def main():
    miles = float(input())
    print(convert_miles_to_roman_paces(miles))


if __name__ == "__main__":
    main()
