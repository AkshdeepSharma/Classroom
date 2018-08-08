import time


# Book Solution


def enumerate_primes(n):
    if n < 2:
        return []
    size = (n - 3) // 2 + 1
    primes = [2]

    is_prime = [True] * size

    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)

            for j in range(2 * i ** 2 + 6 * i + 3, size, p):
                is_prime[j] = False

    return primes

# My Solution


def primes(n):
    if n < 2:
        return []
    prime_numbers = [2]
    for num in range(3, n, 2):
        for index in range(len(prime_numbers)):
            if num % prime_numbers[index] == 0:
                break
        prime_numbers.append(num)
    return prime_numbers


number = 123456

start_time = time.time()
print(enumerate_primes(number))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
#print(primes(number))
print("--- %s seconds ---" % (time.time() - start_time))

print(15//2)