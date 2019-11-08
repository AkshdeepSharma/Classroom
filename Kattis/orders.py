def diff_orders(dpArray, order_cost, items):
    res = []
    if dpArray[order_cost] == -2:
        return "Impossible"
    elif dpArray[order_cost] == -1:
        return "Ambiguous"

    while order_cost > 0:
        res.append(dpArray[order_cost] + 1)
        order_cost -= items[dpArray[order_cost]]
    if order_cost < 0:
        return "Ambiguous"
    res = sorted(res)
    if type(res) == list:
        res = [str(x) for x in res]
    return " ".join(res)


def main():
    num_items = int(input())
    items = list(map(int, input().split()))
    num_orders = int(input())
    orders = list(map(int, input().split()))
    dpArray = [0] + [-2] * 31999

    for i in range(num_items):
        cost = items[i]
        for j in range(30001):
            if dpArray[j] >= 0:
                if dpArray[j + cost] == -2:
                    dpArray[j + cost] = i
                else:
                    dpArray[j + cost] = -1
            if dpArray[j] == -1:
                dpArray[j + cost] = -1

    for i in range(len(orders)):
        print(diff_orders(dpArray, orders[i], items))


if __name__ == '__main__':
    main()
