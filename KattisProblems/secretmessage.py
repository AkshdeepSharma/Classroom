N = int(input())
for _ in range(N):
    original_message = input()
    result = ""
    for K in range(1, 102):
        if K ** 2 >= len(original_message):
            break
    padded_message = original_message + "*" * (K ** 2 - len(original_message))
    K_matrix = [[] for i in range(K)]
    row = 0
    for i in range(len(padded_message)):
        if i != 0 and i % K == 0:
            row += 1
        K_matrix[row].append(padded_message[i])
    for a in range(K):
        for b in reversed(range(K)):
            if K_matrix[b][a] != "*":
                result += K_matrix[b][a]
    print(result)