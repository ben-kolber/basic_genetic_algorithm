import numpy
import time
import random

from dna import dna


class population:
    def __init__(self, pop_size, target):
        self.pop_size = pop_size
        self.target = target
        self.pool = self.generate_pool()

    # population made of DNA objects 
    def generate_pool(self):
        population = []
        for i in range(self.pop_size):
            population.append(dna(self.target))
        return population

    # print score and fitness 
    def print_population(self):
        self.sort_population()
        for i in range(self.pop_size):
            time.sleep(0.01)
            self.pool[i].print_dna()

    # calculate fitness score
    def update_fitness(self):
        for i in range(self.pop_size):
            self.pool[i].fitness(self.target)

    # sort population based on fitness score
    def sort_population(self):
        for i in range(self.pop_size):
            self.pool.sort(key=lambda x: x.score, reverse=True)

    def run_mating_pool(self):
        self.pool = self.mating_pool(0.3)

    # generate a mating pool based on fitness of parents
    # The higher the fitness, the more instances of that parent will 
    # appear in the mating pool 
    # There is also an added mutation factor for every X child
    def mating_pool(self, mutation_rate):
        parents = []
        children = []
        length = len(self.target)
        count = 0
        i = 0

        # creating probability pool of highest ranking parents
        while(count < self.pop_size):
            if (self.pool[i].score == 0):
                parents.append(self.pool[i])
                count += 1
            else:
                for j in range(self.pool[i].score * 2):
                    parents.append(self.pool[i])
                    count += 1
            i += 1

        # take random parents and start creating children
        count = 0
        while (count < self.pop_size):
            choice_one = random.randint(0, self.pop_size-1)
            choice_two = random.randint(0, self.pop_size-1)
            child = dna(self.target)
            child.genes = parents[choice_one].genes[:length/2] + \
                parents[choice_two].genes[length/2:]

            # Add mutation rate
            mutate = random.randint(0, 9)
            if (mutate < mutation_rate * 10):
                # fill in random character
                child.genes[random.randint(0, length-1)] = chr(random.randint(32, 122))

            # add child to new generation
            children.append(child)
            count += 1

        return children
