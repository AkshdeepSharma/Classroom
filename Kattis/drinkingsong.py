def main():
    num_bottles = int(input())
    beverage = input()
    bottles = 'bottles'
    while num_bottles > 1:
        print(
            f'{num_bottles} {bottles} of {beverage} on the wall, {num_bottles} {bottles} of {beverage}.')
        num_bottles -= 1
        if num_bottles == 1:
            bottles = 'bottle'
        print(
            f'Take one down, pass it around, {num_bottles} {bottles} of {beverage} on the wall.')
    print(f'1 bottle of {beverage} on the wall, 1 bottle of {beverage}.')
    print(f'Take it down, pass it around, no more bottles of {beverage}.')


if __name__ == "__main__":
    main()
