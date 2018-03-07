# Coded by Nathan Satterfield
# 11th grade at Francis W. Parker School

import re



# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

dict = open('search_files/dictionary.txt', 'r')
dictionary_list = []

for line in dict:
    words = split_line(line)
    for word in words:
        dictionary_list.append(word)

dict.close()


print("--- Linear Search ---")

alice200_Linear = open('search_files/AliceInWonderLand200.txt' , "r")

def linear_search(key, dictionary_list, line):
    i = 0
    while i < len(dictionary_list) and dictionary_list[i] != key:
        i += 1
    if i < len(dictionary_list) - 1:
        pass
    else:
        print(key, "on line", line, "is not in the dictionary.")


line_count = 0
for line in alice200_Linear:
    words = split_line(line)
    line_count += 1
    for word in words:
        linear_search(word.upper(), dictionary_list, line_count)


alice200_Linear.close()




print(" --- Binary Search ---" )

alice200_Binary = open('search_files/AliceInWonderland200.txt')

def binary_search(key, dictionary_list, line_count):
    lower_bound = 0
    upper_bound = len(dictionary_list) - 1
    found = False

    while not found and lower_bound <= upper_bound:
        middle_pos = (upper_bound + lower_bound) // 2
        if dictionary_list[middle_pos] < key:
            lower_bound = middle_pos + 1
        elif dictionary_list[middle_pos] > key:
            upper_bound = middle_pos - 1
        else:
            found = True

    if not found:
        print(key, "on line", line_count , "is not in the dictionary.")


line_count = 0
for line in alice200_Binary:
    words = split_line(line)
    line_count += 1
    for word in words:
        binary_search(word.upper(), dictionary_list, line_count)