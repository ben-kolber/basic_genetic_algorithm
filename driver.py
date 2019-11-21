from dna import dna
from population import population

import time

pop_size = 200
target = "Hello"


population = population(pop_size, target)

population.update_fitness()
population.print_population()

time.sleep(1)


for i in range(30):
    print("-" * 30)
    print("GENERATION:: {}".format(i))
    print("-" * 30)
    time.sleep(0.1)

    population.run_mating_pool()
    population.update_fitness()
    population.print_population()
