# Book Solution


def buy_and_sell_stock_once(prices):
    min_price_so_far, max_proft = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit


# My Solution


def max_stock_price(A):
    curr_max, buy = 0, A[0]
    for i in range(1, len(A)):
        if buy > A[i]:
            buy = A[i]
        else:
            curr_max = max(curr_max, A[i] - buy)
    return curr_max

