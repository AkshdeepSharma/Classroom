first = "*i*d?"
second = "fabfire"


def match(first, second):
    compare = ""
    answer = ""
    seen = 0
    for ch in range(len(first)):
        if first[ch] == "*":
            bob = ch + seen
            while first[ch + 1] != second[bob]:
                seen += 1
                compare += second[bob]
                bob += 1
            seen -= 1
        else:
            compare += first[ch]
    for ch in range(len(compare)):
        if compare[ch] == '?':
            answer += second[ch]
        else:
            answer += compare[ch]
    if second == answer:
        return True
    return False
print(match(first, second))
