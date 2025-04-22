# What does this piece of code do?
# Answer:rolling two dices, which can pick a number from 1-6,repeatedly until the two showing same number and show the number of trial

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0 #Track the number of attempts
while progress>=0: 
	progress+=1 #Increment attempt counter
	first_n = randint(1,6) #roll the first dice
	second_n = randint(1,6) #roll the secnd dice
	if first_n == second_n: #two dice show the same number
		print(progress) #show the number of trial
		break #Exit the loop

