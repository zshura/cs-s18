word = "lollipop"
current_board = "_" * len(word)

##while current_board != word:
##    guess = input(current_board + "::: Enter a letter: ")
##
##    next_board = ""
##    position = 0
##    while position < len(word):
##        if guess == word[position]:
##            next_board = next_board + guess
##        else:
##            next_board = next_board + current_board[position]
##        position = position + 1
##    current_board = next_board
##print (current_board + " correct!")

for guess_count in range (10): 
    guess = input(current_board + "::: Enter a letter: ")
    next_board = ""
    for position in range(len(word)):
        if guess == word[position]:
            next_board = next_board + guess
        else:
            next_board = next_board + current_board[position]
    current_board = next_board
    if current_board == word:
        break
print(current_board, "Done!")

## THis is a comment
