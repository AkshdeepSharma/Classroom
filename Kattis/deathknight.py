def deathknight(moves):
    count = 0
    for i in range(len(moves)):
        if "CD" in moves[i]:
            count += 1
            continue
    return len(moves) - count


def main():
    n = int(input())
    moves = []
    for _ in range(n):
        moves.append(input())
    print(deathknight(moves))


if __name__ == "__main__":
    main()
