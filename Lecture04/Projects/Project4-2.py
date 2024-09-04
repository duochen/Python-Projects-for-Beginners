import random
import matplotlib.pyplot as plt

# Parameters
population_size = 100
initial_infected = 1
infection_probability = 0.2
recovery_time = 10
simulation_days = 50

# Initialize population (0: healthy, 1: infected, -1: recovered)
population = [0] * population_size
infected_days = [0] * population_size

# Infect the initial population
for i in range(initial_infected):
    population[i] = 1

# Simulation loop
daily_infected = []
for day in range(simulation_days):
    new_infected = 0
    for i in range(population_size):
        if population[i] == 1:
            # Infect others
            for j in range(population_size):
                if population[j] == 0 and random.random() < infection_probability:
                    population[j] = 1
                    new_infected += 1
            
            # Update infection days
            infected_days[i] += 1
            
            # Recover after a certain time
            if infected_days[i] >= recovery_time:
                population[i] = -1
    
    daily_infected.append(new_infected)

# Visualize the results
plt.plot(range(simulation_days), daily_infected, label="Daily Infections")
plt.xlabel("Day")
plt.ylabel("Number of Infected")
plt.title("Epidemic Spread Simulation")
plt.legend()
plt.show()
