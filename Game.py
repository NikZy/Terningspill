#clear window
clear_window = lambda: os.system('cls')
import os
import variables


def start_game ():
 
    #Gets playernames and stores them in a DICITONARY
    players = variables.get_players() 

    loop = True
    while loop:
        #For loop for changin player turns:
        for p in players: 
            print ("")
            print ("")
            print("---------------------------------------------------")
        #Prints players score:
            for name in players:
               print("Score = ", variables.player_name(name, players), ": ", variables.player_score(name, players))
            
            print ("It's " + players[p][0] + "s turn!")
            print ("")
            #Ask player if is ready
            throw_dice = input("Press ENTER to throw the DICE: ")
            if throw_dice == "":
                #Imports round_sum playes one round. Returns the the number the player got this round:
                round_sum = variables.round_sum() 
                
                #Adds round_sum to player score and prints score:
                players[p][1] = players[p][1] + (round_sum) 
                print(players[p][0] + " got a total of: " + str(players[p][1]) + " points!")

                #Checks if we have a winner.
                #If True stops while loop and returns winner, else continous:
                for player in players:
                    if players[player][1] >= 100:
                        loop = False
                if loop == True:
                    new_round = input("Ready for a new round? press ENTER ")
                    clear_window()#clear window
                    while new_round != "":
                        new_round = input("Ready for a new round? press ENTER ")
                    clear_window()#clear window

    winner = variables.find_winner (players)
    return winner


#Starts the game:
winner = start_game ()

clear_window()#clear window
print("The winner is: " + winner)
input("Press ENTER to exit: ")

