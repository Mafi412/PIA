import numpy as np
import random
import copy
import matplotlib.pyplot as plt


NUM_Of_ITEMS = 100
# random.seed(42)
# np.random.seed(42)

random_set = [random.randint(100, 150) for _ in range(NUM_Of_ITEMS)]
np_random_set = np.array(random_set)
value = sum(random_set) // 2

print(value, random_set)


# Population intialization
# Coding used: Characteristic vectors of the subsets (https://en.wikipedia.org/wiki/Indicator_vector)
def random_population(population_size):
    return list(np.random.choice([0, 1], size=(population_size, NUM_Of_ITEMS), replace=True, p=[1/2, 1/2]))


# I want to minimize this fitness, so the smaller the fitness, the better.
# Hence, the term "fitness" is no longer the greatest denotation for this value,
# however it is customary to keep using the term.
def fitness(individual):
    return abs(value - np.sum(individual * np_random_set))


# Tournament selection with elitism (adds the elite as the last selected individual)
def selection(population, fitness_value, k=3):
    contestant_indices = np.random.choice(len(population), size=(len(population) - 1, k))
    fitness_value = np.array(fitness_value)
    
    return [population[tournament_round[np.argmin(fitness_value[tournament_round])]] for tournament_round in contestant_indices] + [population[np.argmin(fitness_value)]]


# One-point crossover with elitism (the last individual is the elite)
def crossover(population, crossover_prob=1):
    new_population = []
    
    for i in range(len(population)//2 - 1):
        individual1 = population[2*i]
        individual2 = population[2*i+1]
        
        if random.random() < crossover_prob:
            # We randomly choose the crossover index
            crossover_point = random.randint(1, len(individual1)-1)
            
            # np.concatanate creates a new array, hence there is no need for the deepcopying
            new_individual1 = np.concatenate([individual1[:crossover_point], individual2[crossover_point:]], axis=0)
            new_individual2 = np.concatenate([individual2[:crossover_point], individual1[crossover_point:]], axis=0)
            
        else:
            new_individual1 = individual1
            new_individual2 = individual2

        new_population.append(new_individual1)
        new_population.append(new_individual2)
        
    new_population.extend(population[-2:])
        
    return new_population


# Bit-flip mutation with elitism (the last individual is the elite)
def mutation(population, individual_mutation_prob=0.1, bit_mutation_prob=0.2):
    new_population = []
    
    for i in range(len(population) - 1):
        individual = population[i]
        
        if random.random() < individual_mutation_prob:
            individual = copy.deepcopy(individual)
            
            for j in range(len(individual)):
                if random.random() < bit_mutation_prob:
                    # This flips 0 to 1 and 1 to 0
                    individual[j] = int(not individual[j])
                        
        new_population.append(individual)
        
    new_population.append(population[-1])
        
    return new_population


# Evolution minimizing the fitness (absolute value of the difference of the sum and the desired value)
def evolution(population_size, max_generations):
    best_fitness = []
    population = random_population(population_size)
    
    for _ in range(max_generations):
        fitness_value = list(map(fitness, population))
        best_fitness.append(min(fitness_value))
        
        parents = selection(population, fitness_value)
        children = crossover(parents)
        mutated_children = mutation(children)
        
        population = mutated_children
        
    # We compute fitness for the last population and obtain the best individual
    fitness_value = list(map(fitness, population))
    best_fitness.append(min(fitness_value))
    best_individual = population[np.argmin(fitness_value)]
    
    # We return our solution (the best individual), the last population and the best fitnesses observed during the algorithm run for logging purposes
    return best_individual, population, best_fitness


best, population, best_fitness = evolution(population_size=100, max_generations=100)

print("Best fitness:", fitness(best))
print("Best individual:", best)

plt.plot(best_fitness)
plt.ylabel("Fitness")
plt.xlabel("Generation")
plt.show()
