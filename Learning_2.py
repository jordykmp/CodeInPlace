'''
LEARNING THE WORLD
On this game each player (players between 1-4) should enter its name, then it will displayed a picture of the continent 
that they are going to learn about, after that the players are going to see some information (3 facts) about at least 10 countries of the continent. 
Then will be displayed 10 questions for each player. Each player will have 30 seconds to answer. The player with the most correct answers is the winner.
'''



import random
import pygame
import time
from pygame import mixer

'''
After that we will define the milestones helper functions
The first thing to do is explain to the users how they will interact with the game, 
and that would be accomplished using a welcome_message() function.
'''

#This function show a welcome message to the players
def welcome_message():
    welcome_1 = 'Welcome to this wonderful game!!!'
    welcome_2 = 'After you play this game, you will be able to know some interesting facts about countries all around the globe'
    welcome_3 = 'Isn\'t that amazing?'
    welcome_4 = 'The rules are simple: '
    rules_1 = '1. The maximum number of players is 4 (1 up to 4)'
    rules_2 = '2. Each player should enter its name'
    rules_3 = '3. Each player will have 30 seconds to answer a question.'
    rules_4 = '4. The player with most correct answers is the winner'
    rules_5 = '5. Have fun while you learn'
    welcome = [welcome_1, welcome_2, welcome_3,'', welcome_4]
    rules = [rules_1, rules_2, rules_3, rules_4, rules_5]
    
    for message in welcome:
        print(message)
        time.sleep(5)   # Delays for 5 seconds.
    print('')
    for rule in rules:
        print(rule)
        time.sleep(5)   # Delays for 5 seconds.
        
'''
As it was explained in the **welcome_message()** function. Now it is time to write the names of the players. 
To accomplish that goal will be necessary to define a new function that validate up to 4 names between the users.
'''
        
#This function will return the number of players with their names
def enter_player_names():
    
    #Choosing number of players with validation
    print('Choice from 1 up to 4 players')
    pls_number = input('Enter the number of players: ')
    pls_number_options=[str(1),str(2),str(3),str(4)]
    while pls_number not in pls_number_options:
        pls_number = input('Please choice 1-4 : ')
    pls_number = int(pls_number)
    
    #Entering the names of the players
    players_dict={1:'',2:'',3:'',4:''}
    for i in range(1,pls_number+1):
        pl_name = input('Enter a name: ')
        players_dict[i] = pl_name

    return players_dict, pls_number
  
  
 #main function
def main():
    welcome_message()
    players_dict, pls_number = enter_player_names()
    
    showing_continent(players_dict, pls_number)
    showing_countries_and_facts(players_dict, pls_number, #other)
                                
    ans_dict = q_and_a(players_dict, pls_number, #other)
    winner = counting_ans(ans_dict,players_dict,pls_number)  
    showing_results(winner, ans_dict,players_dict,pls_number)
