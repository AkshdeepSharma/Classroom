def minimizePriceOfBooks(book_prices):
    cost = 0
    for i in range(len(book_prices)):
        if i % 3 != 0:
            cost += book_prices[i]
    return cost


def main():
    num_books = int(input())
    book_prices = []
    for _ in range(num_books):
        book_prices.append(int(input()))
    print(minimizePriceOfBooks([0] + sorted(book_prices, reverse=True)))


if __name__ == "__main__":
    main()
