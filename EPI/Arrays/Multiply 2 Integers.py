# My solution


def multiply(A, B):
    sign = -1 if (A[0] < 0 ^ B[0] < 0) else 1
    A[0], B[0] = abs(A[0]), abs(B[0])
    result = [0] * (len(A) + len(B))
    for i in reversed(range(len(A))):
        for j in reversed(range(len(B))):
            result[i + j + 1] += A[i] * B[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] = result[i + j + 1] % 10
    num = 0
    while result[num] == 0:
        del result[num]
        num += 1
    result[0] *= sign
    return result

# Book solution


def mult_list(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]


print(mult_list([8, 3, 7], [-9, 1, 2, 3, 4]))

