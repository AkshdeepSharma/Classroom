def eenymeeny(rhyme_length, names):
    curr_group = True
    group1, group2 = [], []
    pos = 0
    while names:
        curr = (pos + rhyme_length) % len(names)
        name = names.pop(curr)
        if curr_group:
            group1.append(name)
        else:
            group2.append(name)
        curr_group = not curr_group
        pos = curr
    return [group1, group2]


def main():
    rhyme = input().split()
    N = int(input())
    names = [input() for _ in range(N)]
    groups = eenymeeny(len(rhyme) - 1, names)
    for group in groups:
        print(len(group))
        for name in group:
            print(name)


if __name__ == "__main__":
    main()
