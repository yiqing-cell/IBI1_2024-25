# Project Plan (Pseudocode):
# 1. Iterate over numbers 1 to 10 to compute each triangular number
# 2. For each number n, calculate the sum of integers from 1 to n
# 3. Display each calculated triangular number

for n in range(1, 11): #displays the first ten values
    triangular_number = sum(range(1, n + 1)) # Calculate the sum from 1 to n
    print(triangular_number) # Display the result