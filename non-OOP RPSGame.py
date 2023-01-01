import random
import os

clear = lambda: os.system('clear')

list_of_choices = ['Rock', 'Paper', 'Scissors']    
        
# declare variables globally here
player_score = 0
computer_score = 0


def check_answer(player_choice, computer_choice):
    
    global player_score
    global computer_score
    
    if player_choice == computer_choice:
        print("Its a draw!")

    elif player_choice == "rock" and computer_choice == "scissors":
        print("Player wins! Rock beats scissors")
        
        player_score += 1

    elif player_choice == "rock" and computer_choice == "paper":
        print("Computer wins! Rock loses to paper")

        computer_score += 1

    elif player_choice == "paper" and computer_choice == "rock":
        print("Player wins! Paper beats rock")

        player_score += 1

    elif player_choice == "paper" and computer_choice == "scissors":
        print("Computer wins! Paper loses to scissors")

        computer_score += 1

    elif player_choice == "scissors" and computer_choice == "paper":
        print("Player wins! Scissors beats Paper")

        player_score += 1

    elif player_choice == "scissors" and computer_choice == "rock": 
        print("Computer wins! Scissors loses to rock")

        computer_score += 1

def game():
        
    global player_score
    global computer_score

    print("Welcome to the game, Rock Paper Scissors!\n ")

    user_input_score = input("What score would you like to cap the game at? If you would like an uncapped game, press enter: ") 
        
    if user_input_score == "":
        
        should_continue = True    
        
        while should_continue:
        
            user_input_choice = input("Choose - Rock, Paper, or Scissors?: ").lower()

            random_computer_choice = random.randint(0,2)

            computer_choice = list_of_choices[random_computer_choice].lower()

            check_answer(user_input_choice, computer_choice)

            print(f"Player score: {player_score} | Computer score: {computer_score}")

            play_again = input("Do you want to play again? Type \"yes\" or \"no\": ").lower()
                
            if play_again == "no":
                print("Program Terminated.")
            
                break         
            
    else:
    
        should_continue = True    

        score_cap = int(user_input_score)

        while should_continue:
            
            user_input_choice = input("Choose - Rock, Paper, or Scissors?: ").lower()

            random_computer_choice = random.randint(0,2)

            computer_choice = list_of_choices[random_computer_choice].lower()

            check_answer(user_input_choice, computer_choice)

            print(f"Player score: {player_score} | Computer score: {computer_score}")

            if score_cap == player_score or score_cap == computer_score:
                should_continue = False

                if player_score == score_cap:
                    print(f"Player wins! 😀 FINAL PLAYER SCORE: {player_score} | FINAL COMPUTER SCORE: {computer_score} ")
                else:
                    print(f"Computer wins! 🖥 FINAL COMPUTER SCORE: {computer_score} | FINAL PLAYER SCORE: {player_score} ")

                play_again = input("Do you want to play a new game? Type \"yes\" or \"no\": ").lower()
                    
                if play_again == "yes":
                    clear()
                    
                    player_score = 0
                    computer_score = 0

                    game()
                else:
                    print("Program Terminated.")
                    break


game()      

    





