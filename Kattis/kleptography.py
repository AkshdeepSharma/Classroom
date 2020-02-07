import string


def kleptography(n, m, plaintext, ciphertext):
    num2alpha = dict(zip(range(0, 26), string.ascii_lowercase))
    alpha2num = dict(zip(string.ascii_lowercase, range(0, 26)))
    pointer = 1
    for i in reversed(range(len(ciphertext))):
        char_num = alpha2num[ciphertext[i]] - alpha2num[plaintext[i]]
        if char_num < 0:
            char_num += 26
        plaintext[m - n - pointer] = num2alpha[char_num]
        pointer += 1
        if "".join(plaintext).isalpha():
            break
    return "".join(plaintext)


def main():
    n, m = map(int, input().split(" "))
    plaintext = ['0'] * (m - n) + list(input())
    ciphertext = list(input())
    print(kleptography(n, m, plaintext, ciphertext))


if __name__ == "__main__":
    main()
