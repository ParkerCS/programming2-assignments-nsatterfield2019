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
file = open('search_files/dictionary.txt' , "r")
all_words = []

for line in file:
    words = split_line(line)
    for words in words:
        all_words.append(words)
#print(all_words)





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
    print(word_length)

average_words = word_length / len(alice_words)
print("The average word length in Alice In Wonder Land is" , average_words)


# CHOOSE ONE OF THE FOLLOWING TWO PROBLEMS

#3 (13pts)  How many times does "Cheshire" occur in"AliceInWonderLand.txt"?
# How many times does "Cat" occur?
# How many times does "Cheshire" immediately followed by "Cat" occur?



#### OR #####

#3  (13pts)Find the most frequently occurring 
#  seven letter word in "AliceInWonderLand.txt"




# CHALLNENGE PROBLEM  (for fun, not for credit).  
#  What words appear in the text of "Alice in Wonderland" that DO NOT occur in "Alice Through the Looking Glass".  Make a list.  You can substitute this for any of the above problems.




