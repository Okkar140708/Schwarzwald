'''
first game random knowledge quiz

IN the first step beginning, I wanna show, some text, then ask directions(left or right), then pop up the quiz

fix the damn exit error

'''
import time
from inputimeout import inputimeout, TimeoutOccurred
import sys
import random



def show_dots(numdots):
    for i in range(numdots):
        print(".", end ="", flush=True)
        time.sleep(0.5)
    print()

player_name = ""
def start():
    global player_name
    player_name = input("PLease, enter your name \n>>  ")
    print(f"Hello {player_name}! \nWelcome to the Black Forest! \n ")
  
    ready_start = ""
    # keep asking player until they are ready to start
    while ready_start != "yes": 
        ready_start  = input("Are you ready to start? \n Yes or No :  ")  
        if ready_start.lower() == "yes":
            time.sleep(1.5)
            print("Great ! Let's begin")
            time.sleep(1)
            exploring()
            break
        elif ready_start.lower() == "no":
            time.sleep(1.5)
            print("Alright!! We can wait until you are reasy.\n Just retype Yes here when you are ready")
        else:
            print("Please reenter Yes or NO")

        

def exploring():
    global player_name
    print("You have just entered the deadly Forest!!\n Be Prepared!!! ")
    time.sleep(1.5)
    print("You are entering the forest now.")
    show_dots(9) # walking into the forest
    print("Oh now! You have to choose one from those two paths in order to continue your journey")
    #first stage either right ot left choosing
    first_stage()
    time.sleep(1)
    second_stage()
    print("Now, you are continuing to explore this forest!!")
    show_dots(5)
    while True:
        print("Oh, now you see two paths, the one is a river and the one is a cave!")
        choosePath = input("Which path would you like to choose? \n type either(River or Cave) : ") # ask the path
        if choosePath.lower() == "river":
            print("Alright! You have chosen the river path. ")
            time.sleep(1)
            print("Now, you will have to complete this game to obtain a boat to continue the journey! ")
            print("Without a boat, there is no chance that you will survive by swimming across this river")
            third_stage()
            break
        elif choosePath.lower() == "cave":
            print("Alright! You have chosen the cave path. ")
            time.sleep(1)
            print("Now, you will have to complete this game to obtain a torch to continue the journey! ")
            print("Without a torch, you will not be able to navigate through this cave.")
            third_stage()
            break
        else:
            print("Invalid input! Please retype either (River or Cave)")
    print("You have successfully completed this game!! : ")
    gift4winnner()

def gift4winnner():
    global player_name
    print(f"{player_name} Huge Congratulation on completing this Schwarzwald")
    time.sleep(1.4)
    print("Here is a gift for you \n ")
    print("https://youtu.be/dQw4w9WgXcQ?si=-25_K22Gxl_lIiuy")
    pass

def third_stage():
   
    show_dots(7)
    print(f"Welcome from the third Stage {player_name}!, which is also the final stage")
    time.sleep(1)
    print("At this stage, you will have to play a game called Tic-TacToe aganist the computer.")
    print("Tic-tac-toe is a two-player game where each player takes turns marking either 'X' or 'O' in a 3x3 grid. \nThe goal is to be the first to get three of your marks in a row, either horizontally, vertically, or diagonally. \nIf all nine spaces are filled without a winner, the game ends in a tie.")
        # display the board
    def display_board(board):
        print('\n')
        print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
        print('---|---|---')
        print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
        print('---|---|---')
        print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
        print('\n')

    # check for winner
    def check_winner(board, mark):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # winning condition
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
        for condition in win_conditions:
            if board[condition[0]] == board[condition[1]] == board[condition[2]] == mark: # 3 possible winning conditions
                return True
        return False

    # Check for tie
    def check_tie(board):
        return ' ' not in board

    # Player move
    def player_move(board, player):
        move = int(input(f"Player {player}, choose your move (1-9): ")) - 1 # list start from 0, but make it user friendly, start from 1
        while board[move] != ' ':
            move = int(input("Invalid move. Choose a different move (1-9): ")) - 1
        board[move] = player

    # computer move
    def computer_move(board, computer, player):
        # block the player's winning move or take a winning move
        for i in range(9):
            copy = board[:] # get a copy of the board
            if copy[i] == ' ':
                copy[i] = computer # simulate placing the computer's mark in that position
                # check if this move results the win for computer, if yes place the computer mark on the bpard and return 
                if check_winner(copy, computer):
                    board[i] = computer
                    return
                copy[i] = player
                # if this blocks a potential winning move for the player, take that move
                if check_winner(copy, player):
                    board[i] = computer
                    return
        # Otherwise, make a random valid move
        move = random.choice([i for i in range(9) if board[i] == ' '])
        board[move] = computer

    attempts = 0 # keep tack the attempts, cuz we will allow only three times to try this game
    print("Welcome to Tic-Tac-Toe!")
    while attempts < 3:
        # Initialize the game
        board = [' '] * 9
        
        
        ready = ""
        while ready != 'yes': # keep asking until the user is ready
            ready = input("Are you ready to start this game?\n type either (Yes or No) : ").lower()
            if ready == 'yes':
                
                player = 'X'
                computer = 'O'
                print("We will choose randomly who will go first.")
                first_turn = random.choice(['player', 'computer']) # randomly choose who will be the first move
                print(f"The {first_turn} goes first!")
                time.sleep(1.5)
                
                game_over = False # initialize the game over at the start of the game
                while True:
                    if first_turn == 'player':
                        display_board(board)
                        player_move(board, player)
                        if check_winner(board, player):
                            display_board(board)
                            print("Player wins!")
                            game_over = True
                            break
                        first_turn = 'computer'
                    else:
                        computer_move(board, computer, player) # let computer choose what to do
                        if check_winner(board, computer):
                            display_board(board)
                            print("Computer wins!")
                            handle_loss4firststage() # a player loses if a computer wins
                            game_over = True
                            break
                        first_turn = 'player'
                    
                    if check_tie(board):
                        display_board(board)
                        print("It's a tie!")
                        break
                if game_over: # break the loop if a player wins
                    break
                attempts += 1 # increment by 1 after finishing the game
                if attempts < 3:
                    print(f"You still have {3-attempts} chance/chances to win this game")
                else:
                    print("You have used all your chances. Therefore, unforutnately, you lose the game")
                    handle_loss4firststage()
                    break

            # if player is still not ready
            elif ready == 'no':
                print("Alright we can wait until you are ready. \n Just retype 'Yes' when you are ready!")

            else:
                print("In valid input! please retype")

def memory_game4secondstage():
    def generate_sequence(length):  # Function to generate a random sequence of numbers
        return [random.randint(1, 9) for _ in range(length)]

    def levels(level_num, length):
        sequence = generate_sequence(length)  # Generate a new sequence based on the level
        print(f"Level {level_num}!")
        time.sleep(1)  # Wait 1 second
        # ask again if user is ready to play this stage
        print("The game is about to start! Just to make sure if you are ready again to memorize the random numbers.")
        ready_start = ""
        # keep asking player until they are ready to start
        while ready_start != "yes": 
            ready_start  = input("Are you ready to start? \n Yes or No :  ")  
            if ready_start.lower() == "yes":
                time.sleep(1.5)
                print("Great ! Let's begin")
                time.sleep(1)
                break
            elif ready_start.lower() == "no":
                time.sleep(1.5)
                print("Alright!! We can wait until you are ready.\n Just retype Yes here when you are ready")
            else:
                print("Please reenter Yes or NO")
        print("Memorize this sequence:")
        print(sequence)
        time.sleep(2.5)
        
        # Push the numbers off the screen by printing multiple new lines
        print("\n"*50)

        # Ask for the user input as a list of integers
        user_input = input("Enter the sequence of numbers you have seen (separated by spaces): ")
        user_sequence = list(map(int, user_input.split()))  # Convert input to a list of integers

        # Check if the user input is correct
        if user_sequence == sequence:
            print("Correct!")
            return True
        else:
            print(f"You are wrong! The correct sequence was: {' '.join(map(str, sequence))}")
            handle_loss4firststage()
            return False

    print("Be Ready! There will be 3 levels that you will have to complete!")
    time.sleep(0.5)

    # Start with Level 1
    if levels(1, 3):
        # Move to Level 2 if Level 1 is correct
        if levels(2, 5):
            # Move to Level 3 if Level 2 is correct
            levels(3, 7)
            print("You have successfully completed level 2. (￣、￣)\nNow, let's continue the journey! (〃￣︶￣)人(￣︶￣〃)")


    

def second_stage():
    print(f"Welcome to the second stage {player_name} !  Keep going ")
    show_dots(5) # keep going
    print("As you go deeper, the forest grows darker, the air colder, and an unsettling silence wraps around you, as if the trees themselves are holding their breath, waiting.")
    time.sleep(2.7)
    print("Ah ha! Now you have to pass this mini game to continue your journey!!")
    time.sleep(2)
    print("This game will be based on recalling short-term memories. You will be given certain amount of time to watch and memorize the random numbers. Then, this game will ask you what that numbers were. You will need to be able to type the numbers exactly that you have seen to pass this stage ")    
    # ask user if ready
    ready_start = ""
    # keep asking player until they are ready to start
    while ready_start != "yes": 
        ready_start  = input("Are you ready to start? \n Yes or No :  ")  
        if ready_start.lower() == "yes":
            time.sleep(1)
            print("Great ! Let's begin")
            time.sleep(0.7)
            memory_game4secondstage()
            break
        elif ready_start.lower() == "no":
            time.sleep(1.2)
            print("Alright!! We can wait until you are ready.\n Just retype Yes here when you are ready")
        else:
            print("Please reenter Yes or NO")
    

def handle_loss4firststage():
   
    """Handles the case when the user loses and decides whether to exit or restart."""
    print("Unfortunately, you have lost this game!")
    choice4lose = input("Would you like to exit or go back to menu and restart the game? (Exit/Menu)\n>> ")
    if choice4lose.lower() == "exit":
        print("Have a nice day!!")
        sys.exit()
        
    elif choice4lose.lower() == "menu":
        return
    else:
        print("Invalid input! Retype either 'Exit' or 'Menu'")


def first_stage():
    
    while True:
        
        Firststage = input("Please Type the dirsctions that you would like to continue (either Right or Left) \n>> ") # ask where to go
        # right or left continue exploring
        if Firststage.lower() == "right":
            print("Ah ha!! You have chosen this path!")
            time.sleep(1)
            print("Here is the Question that you have to answer correctly to continue another stage")
            try:
                # Wait for 10 seconds for user input, otherwise trigger a timeout
                www = inputimeout(prompt="In which country was the WWW(World Wide Web) invented? : ", timeout=10)
                print("You responded: ", www)
                if www.lower() == "switzerland":
                        print("Yay!!! \n You have completed the first stage!")
                        time.sleep(2)
                        print("Now, let's go to the next stage.\n Be prepared !!!")
                        break 
                else:
                    handle_loss4firststage()
                    break
            except TimeoutOccurred:
                # Handle the case when the user takes too long
                print("\nYou took too long to respond! ￣へ￣  \n We can give you a hint. By the way, you will not lose any point if you use the hint. (o゜▽゜)o☆")
                hint = input("Do you want a hint? Type (Yes or No): ")
                if hint.lower() == "yes":
                    print("Here are three countries, and one of them is the correct answer: \n UK or GERMANY or the USA or the Netherlands or Switzerland") # give hint
                    www = input("In which country was the WWW(World Wide Web) invented? : ") # reask the question
                    print("You responded: ", www)
                    #check if the answer is correct
                    if www.lower() == "switzerland":
                        print("Yay!!! \n You have completed the first stage!")
                        time.sleep(2)
                        print("Now, let's go to the next stage.\n Be prepared !!!")
                        break
                    else:
                        handle_loss4firststage()
                        break
                # if user doesn't want hint   
                elif hint.lower() == "no":
                    print("Alright! NO HINT!!!")
                    www = input("In which country was the WWW(World Wide Web) invented? : ") # reask the question
                    print("You responded: ", www)
                    #check if the answer is correct
                    if www.lower() == "switzerland":
                        print("Yay!!! \n You have completed the first stage!") 
                        time.sleep(2)
                        print("Now, let's go to the next stage.\n Be prepared !!!")
                        break
                    else:
                        handle_loss4firststage()
                        break

        elif Firststage.lower() == "left":
            print("Alright! \n You have just chosen left part \n Here is your quiz!")
            try:
                # wait for 10 seconds for user input, otherwise trigger time out
                pythonCountry = inputimeout(prompt="In which country was the Python programming language invented? : ", timeout=10)
                print("You responded: ", pythonCountry)
                if pythonCountry.lower() == "netherlands" or "the netherlands":
                    print("Yay!!! \n You have completed the first stage!")
                    time.sleep(1)
                    print("Now, let's go to the next stage.\n Be prepared !!!")
                    break
                else:
                    handle_loss4firststage()
                    break
            except TimeoutOccurred:
                # Handle the case when the user takes too long
                print("\nYou took too long to respond! ￣へ￣  \n We can give you a hint. By the way, you will not lose any point if you use the hint. (o゜▽゜)o☆")
                hint = input("Do you want a hint? Type (Yes or No): ")
                if hint.lower() == "yes":
                    print("Here are four countries, and one of them is the answer \n The USA \n Switzerland \n Netherlands \n Germany ")
                    pythonCountry = input("In which country was the Python programming language invented? : ")
                    print("You responded: ", pythonCountry)
                    #check if the answer is correct
                    if pythonCountry.lower == "netherlands" or "the netherlands":
                        print("Yay!!! \n You have completed the first stage!")
                        time.sleep(2)
                        print("Now, let's go to the next stage.\n Be prepared !!!")
                        break
                    else:
                        handle_loss4firststage()
                        break
                # if user doesn't want hint   
                elif hint.lower() == "no":
                    print("Alright! NO HINT!!!")
                    pythonCountry = input("In which country was the Python programming language invented? : ")
                    print("You responded: ", pythonCountry)
                    #check if the answer is correct
                    if pythonCountry.lower == "netherlands" or "the netherlands":
                        print("Yay!!! \n You have completed the first stage!")
                        time.sleep(2)
                        print("Now, let's go to the next stage.\n Be prepared !!!")
                   
                    else:
                        handle_loss4firststage()
                        break
        else:
            print(" Invalid input!! Please retype either Right or Left ")
            
            
        

def exit():
    print("Goodbye. Hope to see you again! (^人^) ")


# main start
def main_menu():
    while True:
        print("Welcome To the Schwarzwald Exploration!")
        print("*"*39)
        print("1. Start the Game")
        print("2. Exit")
        choice_option = input("Choose the above two options \n>>  ")
        # conditions for choosing options
        if choice_option == "1":
            start()
        elif choice_option == "2":
            exit()
            break
        else:
            print("Invalid input. Please rewrite either 1 or 2")

main_menu()

