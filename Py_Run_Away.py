###### Dependencies : Python 2.7
###### By Redemption.Man
 
##############################
######## run_away.py #########
##############################
# Keep the O away form the X #
##############################
## redemption.man@gmail.com ##
##############################
 
#controls
#  7 8 9
#   \|/
# 4 - - 6
#   /|\
#  1 2 3
 
#import stuff for random numbers
import random
from random import choice
 
#function to print board
def print_board(b):
    print("")
    print("          "+b[0][0]+b[0][1]+b[0][2]+b[0][3]+b[0][4]+b[0][5]+b[0][6]+b[0][7]+b[0][8]+b[0][9])
    print("          "+b[1][0]+b[1][1]+b[1][2]+b[1][3]+b[1][4]+b[1][5]+b[1][6]+b[1][7]+b[1][8]+b[1][9])
    print("          "+b[2][0]+b[2][1]+b[2][2]+b[2][3]+b[2][4]+b[2][5]+b[2][6]+b[2][7]+b[2][8]+b[2][9])
    print("          "+b[3][0]+b[3][1]+b[3][2]+b[3][3]+b[3][4]+b[3][5]+b[3][6]+b[3][7]+b[3][8]+b[3][9])
    print("          "+b[4][0]+b[4][1]+b[4][2]+b[4][3]+b[4][4]+b[4][5]+b[4][6]+b[4][7]+b[4][8]+b[4][9])
     
    print("          "+b[5][0]+b[5][1]+b[5][2]+b[5][3]+b[5][4]+b[5][5]+b[5][6]+b[5][7]+b[5][8]+b[5][9]+"     "+"  7 8 9")
    print("          "+b[6][0]+b[6][1]+b[6][2]+b[6][3]+b[6][4]+b[6][5]+b[6][6]+b[6][7]+b[6][8]+b[6][9]+"     "+"   \\|/")
    print("          "+b[7][0]+b[7][1]+b[7][2]+b[7][3]+b[7][4]+b[7][5]+b[7][6]+b[7][7]+b[7][8]+b[7][9]+"     "+" 4 - - 6")
    print("          "+b[8][0]+b[8][1]+b[8][2]+b[8][3]+b[8][4]+b[8][5]+b[8][6]+b[8][7]+b[8][8]+b[8][9]+"     "+"   /|\\")
    print("          "+b[9][0]+b[9][1]+b[9][2]+b[9][3]+b[9][4]+b[9][5]+b[9][6]+b[9][7]+b[9][8]+b[9][9]+"     "+"  1 2 3")
    print("")
 
#give player a new position and stops player moving off the board
def player_move(turn, player_pos):
    if turn == 1:
        player_pos[0] = player_pos[0] + 1
        player_pos[1] = player_pos[1] - 1
    elif turn == 2:
        player_pos[0] = player_pos[0] + 1
    elif turn == 3:
        player_pos[0] = player_pos[0] + 1
        player_pos[1] = player_pos[1] + 1
    elif turn == 4:
        player_pos[1] = player_pos[1] - 1
    elif turn == 5:
        player_pos = player_pos
    elif turn == 6:
        player_pos[1] = player_pos[1] + 1
    elif turn == 7:
        player_pos[0] = player_pos[0] - 1
        player_pos[1] = player_pos[1] - 1
    elif turn == 8:
        player_pos[0] = player_pos[0] - 1
    elif turn == 9:
        player_pos[0] = player_pos[0] - 1
        player_pos[1] = player_pos[1] + 1
    else:
        error = 1
    #makes sure player hasnt moved off the game area
    if player_pos[0] < 0 or player_pos[0] > 9 or player_pos[1] < 0 or player_pos[1] > 9:
        error = 1
    else:
        error = 0
    new_pos0 = player_pos[0]
    new_pos1 = player_pos[1]
    return error, new_pos0, new_pos1
 
def comp_move(player_pos, comp_pos):
    if comp_pos[0] < player_pos[0]:
        comp_pos[0] = comp_pos[0] + 1
    if comp_pos[0] > player_pos[0]:
        comp_pos[0] = comp_pos[0] - 1
     
    if comp_pos[1] < player_pos[1]:
        comp_pos[1] = comp_pos[1] + 1
    if comp_pos[1] > player_pos[1]:
        comp_pos[1] = comp_pos[1] - 1
    new_pos0 = comp_pos[0]
    new_pos1 = comp_pos[1]
    return new_pos0, new_pos1
     
#creating the board as a 2d array
b = [[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."]]
 
#setting up game
score = 1
end_game = 0
player_pos = [random.randint(0,9), random.randint(0,9)]
comp_pos = [random.randint(0,9), random.randint(0,9)]
#makes sure player and computer are in different places
while player_pos[0] == comp_pos[0] and player_pos[1] == comp_pos[1]:
    player_pos = [random.randint(0,9), random.randint(0,9)]
    comp_pos = [random.randint(0,9), random.randint(0,9)]
 
     
#the game starts here
while end_game == 0:
    #add player to the board
    b[player_pos[0]][player_pos[1]] = "O"
    #add computer to board
    b[comp_pos[0]][comp_pos[1]] = "X"
     
    print_board(b)
    print("Score : " + str(score))
    print("")
    print
     
    #asks for input then checks input
    while 1 == 1:
        try:
            turn = int(input("Where do you want to move(1-9) : "))
            #check to make sure input is between 1 to 9
            if turn >= 1 and turn <= 9:
                #next line changes the player position for a .
                b[player_pos[0]][player_pos[1]] = "."
                #player move function
                player_move_result = player_move(turn, player_pos)
                error = player_move_result[0]
                player_pos = [player_move_result[1], player_move_result[2]]
                   #checks if that turn has alreay been taking
                if error == 0:
                    score = score + 1
                    break
                else:
                    print("Oops! You can go there. Try again")
            else:
                print("Oops!  That wasnt from 1 to 9.  Try again...")                
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
     
    #computer decides his turn
    #remove compter from game area
    b[comp_pos[0]][comp_pos[1]] = "."
    comp_pos[0], comp_pos[1] = comp_move(player_pos, comp_pos)
 
    #checks if player has been caught
    if player_pos[0] == comp_pos[0] and player_pos[1] == comp_pos[1]:
        end_game = 1
         
#once game has ended
 
#add player to the board this should be overwritten by comp_pos just here to  make sure
b[player_pos[0]][player_pos[1]] = "O"
#add computer to board
b[comp_pos[0]][comp_pos[1]] = "X"
 
print_board(b)
print("Your Final Score is : " + str(score))
print("")
 
