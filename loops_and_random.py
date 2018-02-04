# LOOPS (16pts TOTAL)

import random

# PROBLEM 1 (Fibonacci - 4pts)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.

sequence = 0
fib1 = 1
fib2 = 1
while sequence <= 1000:
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    print(sequence)
    sequence = fib3



# PROBLEM 2 (Dice Sequence - 6pts)
# You roll five six-sided dice, one by one.
# What is the probability that the value of each die
# is greater than OR EQUAL TO the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.
print("\n")
print("\n")
correct = 0
wrong = 0

for i in range(100000):
    roll1 = random.randrange(1, 7)
    roll2 = random.randrange(1, 7)
    roll3 = random.randrange(1, 7)
    roll4 = random.randrange(1, 7)
    roll5 = random.randrange(1, 7)
    if roll2 >= roll1 and roll3 >= roll2 and roll4 >= roll3 and roll5 >= roll4:
        correct += 1
    else:
        wrong += 1
        continue
print("A correct sequence is 1, 1, 4, 5, 6 or any other correct combination.")
print("When the next rolled value is equal to or greater than the previously rolled value")
print("\n")
print("A wrong sequence is 1, 1, 1, 4, 2, 6 or any other wrong combination.")
print("When the next rolled value is less than the previously rolled value")
print("\n")
print("There were", correct , "correct sequences")
print("There were", wrong , "wrong sequences")



# PROBLEM 3 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve. 
