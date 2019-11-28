import random

class dna:
    def __init__(self, target):
        self.length = len(target)
        self.genes = self.create_genes(self.length)
        self.score = 0

    # list of random numbers to represent a gene
    def create_genes(self, length):
        list = []
        for i in range(length):
            list.append(chr(random.randint(32, 122)))
        return(list)

    def print_dna(self):
        print(self.genes)
        print("SCORE: {}".format(self.score))
        print("-"*20)

    # calculate fitness of DNA based on end goal
    def fitness(self, target):
        for i in range(self.length):
            if (self.genes[i] == target[i]):
                self.score += 1
