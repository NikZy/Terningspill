import random


def get_players():
    '''
    (NoneType) -> Dictionary
    Asks for player names
    '''
    players = {}
    question = "Enter name for PLAYER"
    how_many_players = 1  

    #If players {} is empty -> add first player
    if len(players) == 0:
        answer = input(question + str(how_many_players) + ": ")
        answer = answer.strip ()

        loop1 = True
        while loop1:
            if answer != "":
                players[("player"+str(how_many_players))] = [answer, 0]
                print("")
                print("Leave empty to start playing")
                loop1 = False
            else:
                    answer = input(question + str(how_many_players) + ": ")
                    answer = answer.strip ()


    if len(players)>0:
        #Add 1 more player to player count
        how_many_players = how_many_players + 1
        
        #Ask question
        answer = input(question + str(how_many_players) + ": ")
        answer = answer.strip ()
        
        
        #Stops asking only if player leave blank space
        while answer != "":
            loop2 = True
            while loop2: #Ta bort denne loopen

                #Checks if name is taken
                     found_match = False
                     for p in players:
                        if answer in players[p]:
                             found_match = True

                    
                     if found_match == False:
                        #Adds player
                         players[("player" + str(how_many_players))] = [answer, 0]

                        #Add 1 more player to player count
                         how_many_players = how_many_players + 1
                        
                         
                         
                         loop2 = False
                     else:
                         #If name taken:
                         print("Choose a different name!")
                         loop2= False
                         
                    
                #Ask question again
                     answer = input(question + str(how_many_players) + ": ")
                     answer = answer.strip ()


    return players


def dice (): #generates a random number between range 1-6
    '''
    (NoneTypoe) -> int

    Generates a random number between range 1-6
    '''
    
    return random.randint(1, 6)

def round_sum ():
    '''
    (str) -> NoneType

    '''
    round_sum = 0
    loop = True
    print("To throw dice press ENTER! To stop write STOP!")
    print("")
    while loop:
        rnumber = dice()
        if rnumber > 1:
            round_sum = round_sum + rnumber
            print(str(rnumber) + "               " + "sum " + str(round_sum))
            ask = input()
            if ask == "stop" or ask == "STOP":
                print("Your sum for this round is " + str(round_sum))
                print("----------------------------")
                loop = False
        else:
            print("-----------------------------------------------------------")
            print("You got 1! You lose all your points this round!")
            print("-----------------------------------------------------------")
            round_sum = 0
            loop = False
    return round_sum


def player_name (player, dic):
    '''
    (str, dictionary) -> str

    returns the player name

    '''
    name = dic[player][0]
    return name


def player_score (player, dic):
    '''
    (string, dictionary) -> int

    Returns the players score
    '''

    return dic[player][1]

def find_winner (dic):
    '''
    (dicitonary) -> str
    Returns player with most score

    >>> find_winner (
    '''
    if player_score("player1", dic) > player_score("player2", dic):
        return player_name("player1", dic)
    else:
        return player_name("player2", dic)
    


