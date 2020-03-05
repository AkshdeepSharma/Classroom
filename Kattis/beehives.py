from math import sqrt


def countSweetAndSourHives(distance, hives):
    sweet, sour = 0, 0
    for i in range(len(hives)):
        presour = sour
        for j in range(len(hives)):
            if i == j:
                continue
            curr_distance = sqrt(
                (hives[i][0] - hives[j][0]) ** 2 + (hives[i][1] - hives[j][1]) ** 2)
            if curr_distance <= distance:
                sour += 1
                break
        if sour == presour:
            sweet += 1
    return f'{sour} sour, {sweet} sweet'


def main():
    inp = input().split()
    distance, num_hives = float(inp[0]), int(inp[1])
    while distance + num_hives != 0:
        hives = []
        for _ in range(num_hives):
            hives.append(list(map(float, input().split())))
        print(countSweetAndSourHives(distance, hives))
        inp = input().split()
        distance, num_hives = float(inp[0]), int(inp[1])


if __name__ == "__main__":
    main()
