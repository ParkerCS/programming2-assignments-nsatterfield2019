# Coded by Nathan Satterfield
# 11th grade at Francis W. Parker School


'''
Complete the following 3 searching problems using techniques
from class and from Ch15 of the textbook website
'''
import re

# This function takes in a line of text and returns a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

#1.  (7pts) Write code which finds and prints the longest
# word in the provided dictionary.  If there are more
# than one longest word, print them all.  (read the file line by line to accomplish this task)
dict = open('search_files/dictionary.txt', 'r')
dict_words = []

for line in dict:
    words = split_line(line)
    for word in words:
        dict_words.append(word)

longest_words = [len(x) for x in dict_words]
print("The longest word is:", dict_words[longest_words.index(max(longest_words))], "and its length is:" , len(dict_words[longest_words.index(max(longest_words))]))

dict.close()




#2.  (7pts)  Write code which finds
#  The total word count AND average word length of "AliceInWonderLand.txt"
file = open('search_files/AliceInWonderLand.txt' , "r")
alice_words = []

for line in file:
    word = split_line(line)
    for word in word:
        alice_words.append(word)
#print(alice_words)

word_length =0

for word in alice_words:
    word_length += len(word)

print("There are:", word_length, "number of words in Alice In Wonder Land")

average_words = word_length / len(alice_words)
print("The average word length in Alice In Wonder Land is" , average_words)


# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?
file = open('search_files/AliceInWonderLand.txt' , "r")


cat = 0

for line in file:
    word = split_line(line)
    for word in word:
        if word.lower() == "cat":
            cat += 1

print("Cat is said:", cat, "number of times")


file = open('search_files/AliceInWonderLand.txt' , "r")
alice_words = []

for line in file:
    word = split_line(line)
    for word in word:
        alice_words.append(word)

Cheshire = 0

for i in range(len(alice_words)):
    if alice_words[i] == "Cheshire" and alice_words[i + 1].upper() == "CAT":
        Cheshire += 1

print("Cheshire Cat is said:", Cheshire, "number of times")

#### OR #####

#3  (13pts)Find the most frequently occurring 
#  seven letter word in "AliceInWonderLand.txt"




# CHALLNENGE PROBLEM  (for fun, not for credit).  
#  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".
# Make a list.  You can substitute this for any of the above problems.



