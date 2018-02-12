#FUNCTIONS AND IMPORTS (20PTS TOTAL)
# Be sure to comment all your functions as shown in notes

#PROBLEM 1 (how many upper case - 4pts)
# Make a function takes a string as a parameter, then prints how many upper case letters are contained in the string.
# A loop that compares each letter to the .upper() or .lower() of itself will suffice.




# PROBLEM 2 (Biggest, smallest, average - 4pts)
# Make a function which takes 3 numbers as parameters.
# The function then prints the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.

num1 = int(input("Insert a number: "))
num2 = int(input("Insert a different number: "))
num3 = int(input("Insert another different number: "))

print("\n")

average = (num1 + num2 + num3) // 3

print("The average of the numbers is:", average)

high = max(num1, num2, num3)
print("The highest number is:" , high)

low = min(num1, num2, num3)
print("The lowest number is:" , low)

# PROBLEM 4 (add me, multiply me - 4pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.

def sum_product(n1, n2):
    sum = n1 + n2
    product = n1 * n2

    return product, sum



# PROBLEM 5 (Login - 4pts)
# Make a file called import_me.py in this same project
# Inside this new module/file, make a login function which works according to the flow diagram
# PasswordFlowchart.png in this folder
# Substitute your name for Rohan's, and use whatever generic password you want.



# PROBLEM 6 (main - 4pts)
# import the file import_me from Problem 5
# Create a main program using the format if __name__ == "__main__": 
# Place every call from problems 1 through 5 into this program.


