def dominoes(dominoes_dict, l):
    fallen_dominoes = []
    knocked_by_hand = []
    for _ in range(l):
        z = int(input())
        knocked_by_hand.append(z)
        fallen_dominoes.append(z)
    while knocked_by_hand:
        domino = knocked_by_hand.pop()
        if dominoes_dict[domino]:
            knocked_by_hand.extend(dominoes_dict[domino])
            fallen_dominoes.extend(dominoes_dict[domino])
            dominoes_dict[domino] = []
    return(len(set(fallen_dominoes)))


def main():
    num_cases = int(input())
    for _ in range(num_cases):
        dominoes_dict = {}
        n, m, l = map(int, input().split())
        for i in range(1, n + 1):
            dominoes_dict[i] = []
        for _ in range(m):
            dom1, dom2 = map(int, input().split())
            dominoes_dict[dom1].append(dom2)
        print(dominoes(dominoes_dict, l))


if __name__ == '__main__':
    main()
