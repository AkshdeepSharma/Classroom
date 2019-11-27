def determine_weight(weights):
    target_weight = 1000
    best_weight = 0
    visited = set()
    visited.add(0)
    if min(weights) > target_weight:
        return min(weights)
    for weight in weights:
        for value in list(visited):
            curr = abs(1000 - (weight + value))
            if curr == target_weight and best_weight < weight + value:
                best_weight = weight + value
            elif curr < target_weight:
                best_weight = weight + value
                target_weight = curr
            if curr > target_weight and weight + value > 1000:
                continue
            visited.add(weight + value)
    return best_weight


def main():
    num_weights = int(input())
    weights = [int(input()) for weight in range(num_weights)]
    weights = sorted(weights)
    print(determine_weight(weights))


if __name__ == '__main__':
    main()
