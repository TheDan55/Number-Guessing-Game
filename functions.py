from random import randint
import sys
import pprint
import time

scores_easy = []
scores_medium = []
scores_hard = []

def help_command():
    command_dict = {
    'help':"Lists all commands",
    'exit':"Exits the program at any time",
    'highscores':'List highscores of all difficulty levels'
    }
    pprint.pprint(command_dict)

def exit_command():
    print("\n\nExiting the game\n\n. . .\n\nBye!")
    sys.exit()

def list_highscores(scores_easy, scores_medium, scores_hard):
    if len(scores_easy) > 0:
        print(f"\n\nHighscore on easy difficulty: {min(scores_easy)}\n")
    else:
        print("\nNo highscores on easy-level yet.\n")
    
    if len(scores_medium) > 0:
        print(f"\nHighscore on easy difficulty: {min(scores_medium)}\n")
    else:
        print("\nNo highscores on medium-level yet.\n")
    
    if len(scores_hard) > 0:
        print(f"\nHighscore on easy difficulty: {min(scores_hard)}\n")
    else:
        print("\nNo highscores on hard-level yet.\n")

def after_game_menu():
    print("1.New Game\n" \
          "2.Highscores\n" \
          "3.Exit\n")
    
    user_input = input("Please enter the according number: ")
    


    while True:
        if user_input.lower() == "1":
            print("New Game starting. . .")
            difficulty = in_game_menu()
            game(difficulty)
            break
        elif user_input.lower() == "2":
            list_highscores(scores_easy,scores_medium,scores_hard)
            after_game_menu()
        elif user_input.lower() == "3":
            exit_command()
        else:
            print("Invalid. Please try again.")
            after_game_menu()
            
            

def get_difficulty():
    # 1 --> easy
    # 2 --> medium
    # 3 --> hard
    level_selected = True
    while level_selected:
        difficulty_choice = input("Enter your choice: ")
        try:
            difficulty_choice = int(difficulty_choice)
            
            if difficulty_choice in (1, 2 , 3):
                difficulty = difficulty_choice
                level_selected = False
                return difficulty
            else:
                print("Invalid input, try again!")
        except ValueError:
            if difficulty_choice == 'help':
                help_command()
            elif difficulty_choice == 'exit':
                exit_command()
            elif difficulty_choice == 'highscores':
                list_highscores(scores_easy,scores_medium,scores_hard)

            else:
                print("Choose 1, 2 or 3!")

def welcome():
    print("\nWelcome to the Number Guessing Game! \n\n" \
          "I am Thinking of a number betwenn 1 and 100. \n\n" \
          "You have 5 chances to guess the correct number.\n\n")
    
    print("Please select your difficulty level:\n" \
    "1. Easy (10 chances)\n" \
    "2. Medium (5 chances)\n" \
    "3. Hard (3 chances)")

    difficulty_dict = {1:'Easy',
                       2:'Medium',
                       3:'Hard'}

    difficulty = get_difficulty()

    print(f"\nGreat! You have selected the {difficulty_dict[difficulty]} level.\n" \
          "Let's start the game!")
    
    return difficulty


def check_nums(computer_num,player_num):
    player_win = False
    if computer_num < player_num:
        print(f"Incorrect! The number is less than {player_num}")
    if computer_num > player_num:
        print(f"Incorrect! The number is greater than {player_num}")
    if computer_num == player_num:
        player_win = True
        return player_win
    return player_win

def in_game_menu():

    print("Please select your difficulty level:\n" \
    "1. Easy (10 chances)\n" \
    "2. Medium (5 chances)\n" \
    "3. Hard (3 chances)\n" \
    "Type 'help' list all commands.\n\n")

    difficulty_dict = {1:'Easy',
                       2:'Medium',
                       3:'Hard'}

    difficulty = get_difficulty()

    print(f"\nGreat! You have selected the {difficulty_dict[difficulty]} level.\n" \
          "Let's start the game!")
    
    return difficulty

def game(difficulty):


    while True:
        chances_dict = {1:10,
                        2:5,
                        3:3}
        
        chances = chances_dict[difficulty]

        computer_num = randint(1,100)
        attempts = 1
        start = time.time()
        for attempts in range(1,chances+1):
            
            valid_entry = False

            while not valid_entry:
                user_input = input("\nEnter your guess: \n")

                if user_input == 'exit':
                    exit_command()
                elif user_input == 'help':
                    help_command()
                    continue
                elif user_input == 'highscores':
                    list_highscores(scores_easy,scores_medium,scores_hard)
                    continue

                try:
                    int(user_input)
                    valid_entry = True
                except ValueError:
                    print("\nInvalid input! Try again.\n")
            


            player_choice = int(user_input)
            win = check_nums(computer_num,player_choice)


            if win == True and difficulty == 1:
                print(f"\n\nCongratulations! The number was {computer_num}! \n\nYou guessed the number in {attempts} attempts\n\n")
                end = time.time()
                length = round((end - start), 2)
                print(f"It took you {length} seconds to guess the number!")
                scores_easy.append(attempts)
                break
            
            if win == True and difficulty == 2:
                print(f"\n\nCongratulations! The number was {computer_num}! \n\nYou guessed the number in {attempts} attempts")
                end = time.time()
                length = round((end - start), 2)
                print(f"It took you {length} seconds to guess the number!")
                scores_medium.append(attempts)
                break
            if win == True and difficulty == 3:
                print(f"\n\nCongratulations! The number was {computer_num}! \n\nYou guessed the number in {attempts} attempts")
                end = time.time()
                length = round((end - start), 2)
                print(f"It took you {length} seconds to guess the number!")
                scores_hard.append(attempts)
                break

            if attempts == chances:
                print("\n\nYou ran out of the chances!\n" \
                f"The number was: {computer_num}\n\n")
                break



        after_game_menu()
        difficulty = in_game_menu()