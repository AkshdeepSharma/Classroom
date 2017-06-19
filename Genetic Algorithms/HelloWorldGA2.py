#!/usr/bin/env python3
import random

class GeneticAlgorithm(object):
    genome_characters = [chr(i) for i in range(ord(' '), ord('~') + 1)]
    mother_bias = 50/100
    mutation_rate = 70/100
    
    def __init__ (self, target, size):
        
        self.target = target
        self.size = size
        self.population = [self.random_genome(target) for _ in range(size)]
        
    def fitness(self, genome):
        return sum(x != y for x, y in zip(self.target, genome))
    
    def crossover(self, mother, father):
        child = []
        for x, y in zip(mother, father):
            child.append(x if random.random() < self.mother_bias else y)
        if random.random() < self.mutation_rate:
            child[random.randrange(len(child))] = random.choice(self.genome_characters)
        return ''.join(child)
    
    def next_generation(self):
        new_population = sorted(self.population, key = self.fitness)[:len(self.population) >> 1]
        while len(new_population) < len(self.population):
            new_population.append(self.crossover(*random.sample(new_population, 2)))
        self.population = new_population
        
    def random_genome(self, base):
        return "".join(random.choice(self.genome_characters) for _ in range(len(base)))
    
if __name__ == "__main__":
    generation_number = 1
    algorithm = GeneticAlgorithm("Hello, world.", 100)
    while True:
        print(generation_number, min(algorithm.population, key = algorithm.fitness))
        if algorithm.target in algorithm.population:
            break
        generation_number +=1
        algorithm.next_generation()