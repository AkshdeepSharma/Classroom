def hashing_function(sentence):
    hash_val = 0
    for c in sentence:
        hash_val ^= ord(c)
    return hash_val

while True:
    N = int(input())
    hash_storage = {}
    num_collisions = 0
    unique_files = 0
    if N == 0:
        break
    for _ in range(N):
        sentence = input()
        hash_value = hashing_function(sentence)
        if hash_value not in hash_storage:
            hash_storage[hash_value] = [sentence]
        else:
            hash_storage[hash_value].append(sentence)
    
    for key, val in hash_storage.items():
        if len(val) == len(set(val)):
            num_collisions += len(val) * (len(val) - 1) // 2
        else:
            d = {}
            l = []
            running_sum = 0
            for string in val:
                if string not in d:
                    l.append(val.count(string))
                    d[string] = 1
            for i in range(len(l)):
                for j in range(i + 1, len(l)):
                    running_sum += l[i] * l[j]
            num_collisions += running_sum
        unique_files += len(set(val))
    print(str(unique_files) + " " + str(num_collisions))