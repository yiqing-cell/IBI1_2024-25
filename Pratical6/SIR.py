# import necessarylibraries
import numpy as np
import matplotlib.pyplot as plt

N = 10000 # total number of people in the population
Susceptible = N-1 # number of susceptible people that are healthy but may contract the disease
Infected = 1 # number of infected people that have contracted the disease and can pass it on to susceptible people
Recovered = 0 # number of recovered people
beta = 0.3 # infection probability 
gamma = 0.05 # recovery probability

S = [Susceptible] # a list collect number of susceptible people at each time
I = [Infected] # a list collect number of infected people at each time
R = [Recovered] # a list collect number of recovered people at each time
time_steps = 1000 # the number of time step

#Plan
#1.create a loop over 1000 time points to monitor the time course
#2.calculate the population of new infected people
#3.calculate the population of new recovered people
#4.now we can know the new number of susceptible, infected, and recovered individuals
#5.add the new data to the list
#6.draw the plot

for i in range(time_steps):
    new_infected = np.random.choice(range(2), S[i], p=[1 - beta * (I[i] / N), beta * (I[i] / N)]).sum() # calculate the number of new infected people
    new_recovered = np.random.choice(range(2), I[i], p=[1 - gamma, gamma]).sum() # calculate the number of new recovered people
    #record the output of each time step
    S.append(S[i]-new_infected)  # record the total susceptible number
    I.append(I[i]+new_infected-new_recovered) # record the total infected number
    R.append(R[i]+new_recovered) # record the total recovered number
    

# draw the plot
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S, label='Susceptible', color='blue')
plt.plot(I, label='Infected', color='red')
plt.plot(R, label='Recovered', color='green')
plt.xlabel('Ttime')
plt.ylabel('number of people')
plt.title('SIR Model')
plt.legend()
plt.show()
plt.savefig("SIR Model.png") # save the image

