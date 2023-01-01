import random
import os

clear = lambda: os.system('clear')

from enum import Enum
class RPSChoice(Enum):
    ROCK = 1
    PAPER= 2
    SCISSORS = 3

class RPSGame:  
    def __init__(self) -> None:    #constructor
        self.player_score = 0  #EVERY new object has these attributes 
        self.computer_score = 0
        self.is_infinite_mode = None

    def start(self):
        print("\nNEW GAME STARTED\n")
        ans = input("Do you want to play infinite mode?: (y/n) ")

        while ans.lower() != "y" and ans.lower() != "n":
          print("Not a valid answer")
          ans = input("Do you want to play infinite mode?: (y/n) ")

        if ans.lower() == "y": 
          self.is_infinite_mode = True
          self.infinite_path()

        elif ans.lower() == "n":
            self.is_infinite_mode = False
            self.cap_path()

    def cap_path(self):
        ans_scorecap = (input("Input a score cap: "))
        list_of_choices = [1, 2, 3]
        should_continue = True
        
        while should_continue:
            player_choice = int(input("""\nPlay!

1 - 🪨 
2 - 📄 
3 - ✂ 

YOUR CHOICE: """))
            random_num = random.randint(0,2)
            computer_choice = list_of_choices[random_num]

            self.check_answer(player_choice, computer_choice)
            self.print_score()

            if int(ans_scorecap) == self.player_score or int(ans_scorecap) == self.computer_score:
                    should_continue = False
                    self.conclude_winner()
                    play_again = input("Do you want to play a new game? Type \"y\" or \"n\": ").lower()
                
                    while play_again != "y" and play_again != "n":
                        print("Not a valid answer! ")
                        play_again = input("Do you want to play a new game? Type \"y\" or \"n\": ").lower()
                    
                    if play_again == "y":
                        clear()
                        self.clear_score()
                        self.cap_path()
                    
                    elif play_again == "n": 
                        print("\nProgram terminated... ")
                        break
                        




    def infinite_path(self):
        should_continue = True    
        while should_continue:
            player_choice = int(input("""\nPlay!

1 - 🪨 
2 - 📄 
3 - ✂ 

YOUR CHOICE: """))

            list_of_choices = [1,2,3]
            random_computer_choice = random.randint(0,2)
            computer_choice = list_of_choices[random_computer_choice]

            random_num = random.randint(0,2)
            computer_choice = list_of_choices[random_num]
            self.check_answer(player_choice, computer_choice)
            self.print_score()

            play_again = input("Do you want to play again? Type \"y\" or \"n\": ").lower()

            while play_again != "y" and play_again != "n":
                print("Not a valid answer! ")
                play_again = input("Do you want to play again? Type \"y\" or \"n\": ").lower()
            
            if play_again == "n":
                should_continue = False
                self.conclude_winner()
                break            


    def conclude_winner(self):
        """
        This method ... 
        """
        if self.player_score > self.computer_score:
            print(f"\nPLAYER WINS! 😀 FINAL PLAYER SCORE: {self.player_score} | FINAL COMPUTER SCORE: {self.computer_score}\n ")
        elif self.player_score < self.computer_score:
            print(f"\nCOMPUTER WINS! 🖥  FINAL COMPUTER SCORE: {self.computer_score} | FINAL PLAYER SCORE: {self.player_score}\n ")        
        else:
            print(f"\nA TIE! 👔 FINAL PLAYER SCORE: {self.player_score} | FINAL COMPUTER SCORE: {self.computer_score}\n ")

    def clear_score(self):
        self.player_score = 0
        self.computer_score = 0

    def print_score(self):
        print(f"\nCURRENT PLAYER SCORE: {self.player_score} | CURRENT COMPUTER SCORE: {self.computer_score}\n ")

    def check_answer(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            print("Its a draw! ❌ " )

        elif player_choice == 1 and computer_choice == 3:
            print("PLAYER WINS! 😀 ||| 🪨  🤜 ✂ ")
            self.player_score += 1
            
        elif player_choice == 1 and computer_choice == 2:
            print("COMPUTER WINS! 🖥  ||| 🪨  🤛 📄")
            self.computer_score += 1    

        elif player_choice == 2 and computer_choice == 1:
            print("PLAYER WINS! 😀 ||| 📄 🤜 🪨")
            self.player_score += 1        

        elif player_choice == 2 and computer_choice == 3:
            print("COMPUTER WINS! 🖥  ||| 📄  🤛 ✂")
            self.computer_score += 1

        elif player_choice == 3 and computer_choice == 2:
            print("PLAYER WINS! 😀 ||| ✂  🤜 📄")
            self.player_score += 1

        elif player_choice == 3 and computer_choice == 1: 
            print("COMPUTER WINS! 🖥  ||| ✂  🤛 🪨")
            self.computer_score += 1



