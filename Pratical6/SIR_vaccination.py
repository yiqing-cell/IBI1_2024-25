# import necessarylibraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000 # total number of people in the population
beta = 0.3 # infection probability 
gamma = 0.05 # recovery probability
vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.figure(figsize=(6, 4), dpi=150)
for v_rate in vaccination_rates:
    V = int(N * v_rate)  # number of vaccinated people
    Susceptible = max(N - V - 1,0)  # number of susceptible people that are healthy but may contract the disease
    Infected = 1  # number of infected people that have contracted the disease and can pass it on to susceptible people
    if V == N :
        Infected = 0
    Recovered = 0  # number of recovered people
    S = [Susceptible]
    I = [Infected]
    R = [Recovered]
    time_steps = 1000
    #Plan
    #1.create a loop over 1000 time points to monitor the time course
    #2.calculate the population of new infected people
    #3.calculate the population of new recovered people
    #4.now we can know the new number of susceptible, infected, and recovered individuals
    #5.add the new data to the list
    #6.draw the plot
    for i in range(time_steps):
        new_infected = np.random.choice([0,1], S[i], p=[1 - beta * (I[i] / N), beta * (I[i] / N)]).sum()
        new_recovered = np.random.choice([0,1], I[i], p=[1 - gamma, gamma]).sum()
        S.append(max(S[i]-new_infected, 0))
        I.append(max(I[i]+new_infected-new_recovered, 0))
        R.append(max(R[i]+new_recovered, 0))
    # draw the plot
    plt.plot(I, label=f'Vaccination {int(v_rate*100)}%', color=cm.viridis(30))

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR Model with different vaccination rate')
plt.legend()
plt.savefig("SIR_vaccination.png")
plt.show()