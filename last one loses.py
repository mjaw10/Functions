import random
import time

#Functions

def counters():
    counter_input = int(input("Please enter the amount of counters you want to use (10-50)\n"))
    while counter_input < 10 or counter_input > 50:
        print("That is not between 10 and 50. Try again.")
        counter_input = int(input("Please enter the amount of counters you want to use (10-50)\n"))
    no_counters = counter_input
    return no_counters

def user_turn(no_counters):
    user_counters = int(input("How many counters do you want to take? (you can take up to 3)\n"))
    while user_counters < 1 or user_counters > 3:
        print("That is not between 1 and 3. Try again.")
        user_counters = int(input("How many counters do you want to take?\n"))
    no_counters = no_counters - user_counters
    print()
    if no_counters == 1:
        print("There is {0} counter left".format(no_counters))
    else:
        print("There are {0} counters left".format(no_counters))
    print()
    return no_counters

def computer_turn_random(no_counters):
    print("Computers turn")
    time.sleep(2)
    computer_counters = random.randint(1,3)
    no_counters = no_counters - computer_counters
    print("The computer has taken {0} counters".format(computer_counters))
    print()
    print("There are {0} counters left".format(no_counters))
    print()
    return no_counters

def computer_turn_playing(no_counters):
    print("Computers turn")
    time.sleep(2)
    if no_counters == 5:
        no_counters = 4
        print("The computer has taken 1 counter")
        print("There are 4 counters left")
    elif no_counters == 4:
        no_counters = 1
        print("The computer has taken 3 counters")
        print("There is 1 counter left")
    elif no_counters == 3:
        no_counters = 1
        print("The computer has taken 2 counters")
        print("There is 1 counter left")
    elif no_counters == 2:
        no_counters = 1
        print("The computer has taken 1 counter")
        print("There is 1 counter left")
    elif no_counters == 1:
        no_counters = 0
        print("The computer has taken 1 counter")
        print("There is 0 counters left")
    return no_counters

def player_v_player():
    player_1 = input("What is player 1's name?\n")
    player_2 = input("What is player 2's name?\n")
    player_1 = player_1.title()
    player_2 = player_2.title()
    
    program = "y"
    player_1_score = 0
    player_2_score = 0
    while program == "y" or program == "Y":
        no_counters = counters()
        turn = "player_1"
        while no_counters > 0:
            if turn == "player_1":
                print("{0}'s turn".format(player_1))
                no_counters = user_turn(no_counters)
                turn = "player_2"
            elif turn == "player_2":
                print("{0}'s turn".format(player_2))
                no_counters = user_turn(no_counters)
                turn = "player_1"
                
        if turn == "player_1":
            print("{0} wins!".format(player_1))
            player_1_score = player_1_score + 1
        elif turn == "player_2":
            print("{0} wins!".format(player_2))
            player_2_score = player_2_score + 1
        print()
        print(" The score is: \n    {0}: {1} \n    {2}: {3}".format(player_1,player_1_score,player_2,player_2_score))
        print()
        program = input("Would you like to play again? (y/n)\n")

def player_v_computer():
    name = input("What is your name?\n")
    name = name.title()
    program = "y"
    player_score = 0
    computer_score = 0
    while program == "y" or program == "Y":
        no_counters = counters()
        turn = "user"
        while no_counters > 5:
            if turn == "user":
                print("Your Turn")
                no_counters = user_turn(no_counters)
                turn = "com"
            elif turn == "com":
                no_counters = computer_turn_random(no_counters)
                turn = "user"
                
        while no_counters > 0:
            if turn == "user":
                print("Your turn")
                no_counters = user_turn(no_counters)
                turn = "com"
            elif turn == "com":
               no_counters = computer_turn_playing(no_counters)
               turn = "user"

        print()
        if turn == "com":
            print("You lose!")
            computer_score = computer_score + 1
        elif turn == "user":
            print("Well done! You win!")
            player_score = player_score + 1
            
        print()
        print(" The score is: \n    {0}: {1} \n    Computer: {2}".format(name,player_score,computer_score))
        print()
        program = input("Would you like to play again? (y/n)\n")
    
#Main program


print("This is last one loses")
print("If you take the last counter you lose!")
print()
print("Which game would would you like to play? \n \n 1. Player vs Player \n 2. Player vs Computer")
print()
game_type = int(input("Enter the number corrosponding to the program you want to run\n"))

if game_type == 1:
    player_v_player()
elif game_type == 2:
    player_v_computer()
              
