# import necessarylibraries
import numpy as np
import matplotlib.pyplot as plt

size = 100 # the size of array
beta = 0.3  # infection probability
gamma = 0.05  # recovery probability
time_steps = 100  # the total number of time steps

#Plan:
#1. Initialize a 100×100 population array with one random infection.  
#2. Identify infected individuals using coordinate detection.  
#3. Process recoveries by transitioning infected individuals to recovered state with probability γ.  
#4. Spread infection to susceptible neighbors in four directions with probability β.  
#5. Update the array.  
#6. Visualize the process using heatmap.  
#7. Save snapshots at key time points (t=0,10,50,99).   

# make array of all susceptble population
population = np.zeros((100,100))
# randomly choose one infected
outbreak = np.random.randint(0, size, 2)
population[outbreak[0], outbreak[1]] = 1

colors = {0: 'purple', 1: 'blue', 2: 'yellow'} # susceptible individuals in dark purple, infected individuals in blue-green and recovered individuals in yellow
plt.figure(figsize=(6,4), dpi=150) #set up figure

for t in range(time_steps): # Iterates over each time step
    new_population = population.copy() # Create a copy of the current state
    infected_indices = np.argwhere(population == 1) # Find all infected individuals

    for x, y in infected_indices:
        # stimulate recovery 
        if np.random.rand() < gamma:
            new_population[x, y] = 2
        
        # stimulate disease spreading
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #find the neighbors of infected person
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and population[nx, ny] == 0:
                if np.random.rand() < beta:
                    new_population[nx, ny] = 1
    
    population = new_population.copy()
    
    # draw heat map
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.title(f'Time Step {t}')
    plt.pause(0.1)
    if t == 0:
        plt.savefig("time step 0.png") # save the image at time step 0
    if t == 10:
        plt.savefig("time step 10.png") # save the image at time step 10
    if t == 50:
        plt.savefig("time step 50.png") # save the image at time step 50
    if t == 99:
        plt.savefig("time step 99.png") # save the image at time step 99
plt.show()
