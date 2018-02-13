# Paired with functions_and_imports.py homework
# For problem #5 on the homework
# Password Problem

password_correct = "3507robotheosis"

def login(user_name, password):
    '''
    :param user_name: takes in users name
    :param password: takes in users password based off of theier account name
    :return:
    '''
    if user_name == "Rowan":
        if password == password_correct:
            print("Welcome.")
        else:
            print("Incorrect.")
    else:
        print("Access denied.")
