import random
import string

def hamming_distance(s1,s2):
    if len(s1) != len(s2):
        return float('inf')
    
    return sum (c1 != c2 for c1, c2 in zip(s1,s2))

def get_random_character():
    return random.choice(string.printable)

def get_random_string(length):
    return ''.join(get_random_character() for _ in range(length))

def make_child(p1, p2):
    f1, f2 = map(fitness, [p1, p2])
    child = ''
    for c1, c2 in zip(p1, p2):
        if random.random() < mutation_rate:
            child += get_random_character()
        else:
            child += random.choice(c1*f1 + c2*f2)
    return child

generation_size = 100

target = input()
mutation_rate = 1/len(target)
fitness = lambda s: hamming_distance(s, target)

population = set([get_random_string(len(target)) for _ in range(generation_size)])
generation_count = 1

while True:
    fittest = min(population, key = fitness)
    score = fitness(fittest)
    
    print(generation_count, score, fittest)
    if score == 0:
        print('SUCCESS!')
        break
    
    parent1 = fittest
    parent2 = min((population - set([parent1])), key = fitness)
    
    population = set(make_child(parent1, parent2) for _ in range(generation_size))
    generation_count += 1