def odd_man_out(guests):
    guests_dict = {}
    for guest in guests:
        if guest not in guests_dict:
            guests_dict[guest] = 1
        else:
            guests_dict.pop(guest)
    for key in guests_dict.keys():
        return key


def main():
    N = int(input())
    for i in range(1, N + 1):
        num_guests = input()
        guests = input().split()
        guest = odd_man_out(guests)
        print("Case #" + str(i) + ": " + guest)


if __name__ == '__main__':
    main()
