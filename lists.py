#LISTS (31PTS TOTAL)
#In these exercises you should should use functions as needed.  All functions should have comments to describe their purpose.

import random

# PROBLEM 1 (Using List Comprehensions - 6pts)
# Use the list comprehension method to do the following:
# a) Make a list of numbers from 1 to 100
# b) Make a list of even numbers from 20 to 40
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)

numbers = []
for i in range(1, 101):
    numbers.append(i)

print(numbers)


even_num = []
for i in range(20, 41):
    if i % 2 == 0:
        even_num.append(i)

print(even_num)



squares = [x ** 2 for x in range(100)]
print(squares)


#PROBLEM 2 (8-ball - 5pts)
# A magic 8-ball, when asked a question, provides a random answer from a list.
# The code below contains a list of possible answers. Create a magic 8-ball program that
# prints a random answer.
answer_list = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]

input("Ask a question:")
print(random.choice(answer_list))


# PROBLEM 3 (Shuffle - 5pts)
# A playing card consists of a suit (Heart, Diamond, Club, Spade) and a value (2,3,4,5,6,7,8,9,10,J,Q,K,A).
# Create a list of all possible playing cards, which is a deck.
# Then create a function that shuffles the deck, producing a random order.

suits = ["S", "H", "C", "D"]
numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

deck = []
for suit in suits:
    for number in numbers:
        deck.append(suit + number)

print(deck)


deck_new = []
while len(deck) > 0:
    print(len(deck_new))
    draw = deck.pop(random.randrange(len(deck)))
    deck_new.append(draw)
print(deck_new)


# PROBLEM 4 (Tic-Tac-Toe - 15pts)
# Write a Tic-Tac-Toe program that allows two people to play the game against each other.
# In turn, ask each player which row and column they want to play.
# Make sure that the program checks if that row/column combination is empty.
# When a player has won, end the game.
# When the whole board is full and there is no winner, announce a draw.
# This is a fairly long program to write (60 lines or so).
# It will definitely help to use some functions.
# I recommend that you create a function display_board() that gets the board
# as parameter and displays it,
# a function get_row_column() that asks for a row or a column (depending on a parameter)
# and checks whether the user entered a legal value,
# and a function winner() that gets the board as argument and checks if there is a winner.
# Keep track of who the current player is using a global variable player that you can
# pass to a function as an argument if the function needs it.
# I also use a function opponent(), that takes the player as argument and returns
# the opponent. I use that to switch players after each move.

# The main program will be something along the lines of (in pseudo-code):
# display board
# while True:
#   ask for row
#   ask for column
#       if row/column already occupied:
#           display error
#   place player marker in row/col
#   display board
#   check for winner:
#       announce winner
#       break
#   check board full:
#       announce draw
#       break
#   switch player

def draw_board(draw):
    print(draw[0][0], draw[0][1], draw[0][2])
    print(draw[1][0], draw[1][1], draw[1][2])
    print(draw[2][0], draw[2][1], draw[2][2])

def check_win(board,player):
    if board[0][0] == player and board[0][1] == player and board[0][2] == player: # row 1
        return True

    elif board[1][0] == player and board[1][1] == player and board[1][2] == player: # row 2
        return True

    elif board[2][0] == player and board[2][1] == player and board[2][2] == player: # row 3
        return True

    elif board[0][0] == player and board[1][0] == player and board[2][0] == player: # column 1
        return True

    elif board[0][1] == player and board[1][1] == player and board[2][1] == player: # column 2
        return True

    elif board[0][2] == player and board[1][2] == player and board[2][2] == player: # column 3
        return True

    elif board[0][0] == player and board[1][1] == player and board[2][2] == player: # diag 1 left to right
        return True

    elif board[0][2] == player and board[1][1] == player and board[2][0] == player: # diag 2 right to left
        return True

    else:
        return False

def check_full(board):
    for row in board:
        if " " in row:
            return False
    else:
        return True

done = False
board = [[" ", " ", " "],[" ", " ", " "], [" ", " ", " "]]
draw_board(board)
player = "X"





while not done:
    row = int(input("player " + player + " Enter row (1,2,3): "))
    col = int(input("player " + player + " Enter col (1,2,3): "))
    if board[row-1][col-1] == " ":
        board[row - 1][col - 1] = player
    else:
        print("That space is taken")
        continue
    draw_board(board)
    if check_win(board,player):
        print(player, "wins!!")
        break
    if check_full(board):
        print("Draw!")
        break
    if player == "X":
        player = "O"
    else:
        player = "X"




# CHALLENGE PROBLEM 5 (MAY DO AS SUBSTITUTE FOR PROBLEM 4, NO ADDITIONAL CREDIT)
# Create a program that is a simplified version of the game “Battleship.”
# The computer creates (in memory) a grid that is 4 cells wide and 3 cells high.
# The rows of the grid are numbered 1 to 3, and the columns of the grid are labeled A to D.
# The computer hides a battleship in three random cells in the grid.
# Each battleship occupies exactly one cell.
# Battleships are not allowed to touch each other horizontally or vertically.
# Make sure that the program places the battleships randomly, so not pre-configured.
# The computer asks the player to “shoot” at cells of the grid.
# The player does so by entering the column letter and row number of the cell
# which she wants to shoot at (e.g., "D3").
# If the cell which the player shoots at contains nothing, the computer responds with “Miss!”
#  If the cell contains a battleship, the computer responds with “You sunk my battleship!”
# and removes the battleship from the cell (i.e., a second shot at the same cell is a miss).
# As soon as the player hits the last battleship, the computer responds with displaying
# how many shots the player needed to shoot down all three battleships, and the program ends.
# To help with debugging the game, at the start the computer should display the grid with
# O's marking empty cells and X's marking cells with battleships.
# Hint: If you have troubles with this exercise, start by using a board which has the
# battleships already placed.
# Once the rest of the code works, add a function that places the battleships at random,
# at first without checking if they are touching one another.
# Once that works, add code that disallows battleships touching each other.
