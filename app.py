"""
This is the main code of my program, Guess the number !!!
"""
import random
import time

secretNumber= random.randint(1, 100)
# Functions
def get_guess_player():
       time.sleep(2)
       global number
       number= int(input("I'ts your turn, please guess the number, write it down here:"))
       return number

def get_guess_computer():
      time.sleep(2)
      global computerNumber
      computerNumber= random.randint(1, 100)
      return computerNumber

def evaluate_guess(guess):
    if guess == secretNumber:
        print("Congratulations! You won...")
        return True
    elif guess > secretNumber:
        print('Too high')
    else:
        print('Too low')
    return False
    
   
def mainFunction():    
    flag_for_break_loop= True
    while flag_for_break_loop:
        print("##### Player's turn ####")
        player_guess= get_guess_player()
        time.sleep(2)
        if evaluate_guess(player_guess):
            flag_for_break_loop= False
            break
        
        
        print("#### Computer's turn ####")
        computer_guess= get_guess_computer()
        print(f"It's the computer's turn: {computer_guess} ")
        time.sleep(2)
        if evaluate_guess(computer_guess):
            flag_for_break_loop= False
            break
        
    print(flag_for_break_loop)   
    return flag_for_break_loop
       

if __name__ == '__main__':
    mainFunction()
    get_guess_computer()
    get_guess_player()
    evaluate_guess()


