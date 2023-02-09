population = [int(x) for x in input().split(', ')]
threshold_wealth = int(input())

distribution_doesn_t_possible = False
for unit in range(len(population)):
    wealthest_index = population.index(max(population))
    if unit != wealthest_index and population[unit] < threshold_wealth:
        given_value = threshold_wealth - population[unit]
        if population[wealthest_index] - given_value < threshold_wealth:
            distribution_doesn_t_possible = True
            break
        population[wealthest_index] -= given_value
        population[unit] += given_value

if not distribution_doesn_t_possible:
    print(population)
else:
    print('No equal distribution possible')
# This task is not assessed from the judge!