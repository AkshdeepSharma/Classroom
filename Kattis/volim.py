def main():
    MAX_TIME = 210
    curr_time = 0
    exploding_player = None
    start = int(input())
    questions = int(input())
    for _ in range(questions):
        query = input().split()
        time, correctness = int(query[0]), query[1]
        curr_time += time
        if curr_time >= MAX_TIME and not exploding_player:
            exploding_player = start
        if correctness == 'T':
            if start == 8:
                start = 1
            else:
                start += 1
    print(exploding_player)


if __name__ == "__main__":
    main()
