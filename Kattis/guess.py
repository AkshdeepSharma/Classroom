def binary_search(lower, upper):
    mid = (lower + upper) // 2
    return mid


lower, upper = 1, 1001
while True:
    mid = binary_search(lower, upper)
    print(mid)
    guess = input()
    if guess == "lower":
        upper = mid
    elif guess == "higher":
        lower = mid
    else:
        break
    binary_search(lower, upper)
