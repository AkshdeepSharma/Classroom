# Book Solution


def buy_and_sell_stock_twice(prices):
    max_total_profit, min_price_so_far = 0.0, float('inf')
    first_buy_sell_profits = [0] * len(prices)

    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    max_price_so_far = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(max_total_profit, max_price_so_far - price + first_buy_sell_profits[i - 1])

    return max_total_profit


# My Solution (I read question wrong)


def max_profit(A):
    max_money = 0
    for i in range(2):
        curr_profit, index = 0, 0
        buy = A[0]
        for j in range(1, len(A)):
            if buy > A[j]:
                buy = A[j]
            else:
                if A[j] - buy > curr_profit:
                    curr_profit = A[j] - buy
                    index = A.index(buy)
        max_money += curr_profit
        del A[index]
    return max_money


array = [60, 20, 40, 40, 80, 0]
print(buy_and_sell_stock_twice(array))
print(max_profit(array))