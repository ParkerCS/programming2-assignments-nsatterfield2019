# Coded by Nathan Satterfield
# 11th grade at Francis W. Parker School


import import_me


#FUNCTIONS AND IMPORTS (20PTS TOTAL)
# Be sure to comment all your functions as shown in notes

#PROBLEM 1 (how many upper case - 4pts)
# Make a function takes a string as a parameter, then prints how many upper case letters are contained in the string.
# A loop that compares each letter to the .upper() or .lower() of itself will suffice.

def string(string_input):
    '''
    Prints # of upper case letters
    :param string_input:
    :return:
    '''
    letters_uppercase = 0
    for letters in string_input:
        if letters == letters.upper():
            letters_uppercase += 1
    print(letters_uppercase)


# PROBLEM 2 (Biggest, smallest, average - 4pts)
# Make a function which takes 3 numbers as parameters.
# The function then prints the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.


def num_parameters(num1, num2, num3):
    '''
    :param num1: number 1
    :param num2: number 2
    :param num3: number 3
    :return: average, high number, low number
    '''
    average = (num1 + num2 + num3) // 3
    print("The average of the numbers is:", average)
    high = max(num1, num2, num3)
    print("The highest number is:", high)
    low = min(num1, num2, num3)
    print("The lowest number is:", low)

# PROBLEM 4 (add me, multiply me - 4pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.

def sum_product(n1, n2):
    '''
    :param n1: number 1
    :param n2: number 2
    :return: product and sum of n1 and n2
    '''
    sum = n1 + n2
    product = n1 * n2

    return product, sum



# PROBLEM 5 (Login - 4pts)
# Make a file called import_me.py in this same project
# Inside this new module/file, make a login function which works according to the flow diagram
# PasswordFlowchart.png in this folder
# Substitute your name for Rohan's, and use whatever generic password you want.

'''
This can be found on the "import_me.py" file
'''

# PROBLEM 6 (main - 4pts)
# import the file import_me from Problem 5
# Create a main program using the format if __name__ == "__main__": 
# Place every call from problems 1 through 5 into this program.

if __name__ == "__main__":
    string("Inspire Award, Control Award, and Winning Alliance 1st pick")               # from problem 1
    num_parameters(6, 14, 2900)                                                         # from problem 2
    print(sum_product(54, 900))                                                         # from problem 4
    import_me.login("Rowan", "3507robotheosis")                                         # from problem 5
