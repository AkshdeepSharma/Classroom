def max_profit(prices):
    max_difference = 0
    start = prices[0]
    for i in prices[1:]:
        if i > start:
            max_difference += i - start
        start = i
    return max_difference
