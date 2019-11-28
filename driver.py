from dna import dna
from population import population

# size of a population
pop_size = 200
# target string population will end up generating
# starting from a random string
target = "Hello"

population = population(pop_size, target)
population.update_fitness()
population.print_population()

# range is the number of generations that will be created 
for i in range(30):
    print("-" * 30)
    print("GENERATION:: {}".format(i))
    print("-" * 30)
    time.sleep(0.1)
    population.run_mating_pool()
    population.update_fitness()
    population.print_population()
