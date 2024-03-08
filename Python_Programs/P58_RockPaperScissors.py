'''
Simplified Version of the Code

import random
gameComponenets = ['rock','paper','scissors']
a = random.randint(0,2)
computer = gameComponenets[a]
user = input("Enter Your Choice: ").lower()
print("Computer Chooses: ",computer.capitalize())
if user == computer:
    print("Draw")
elif user == 'rock':
    if computer == 'paper':
        print("Computer Wins")
    elif computer == 'scissors':
        print("You Win")
elif user == 'scissors':
    if computer == 'rock':
        print("Computer Wins")
    elif computer == 'paper':
        print("You Win")
elif user == 'paper':
    if computer == 'rock':
        print("You Win")
    if computer == 'scissors':
        print("Computer Wins")
'''
import random
def get_user_choice():
    while True:
        user_input = input("Enter Your Choice (rock/paper/scissors): ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def determine_winner(user, computer):
    outcomes = {
        ('rock', 'paper'): 'Computer Wins',
        ('rock', 'scissors'): 'You Win',
        ('paper', 'rock'): 'You Win',
        ('paper', 'scissors'): 'Computer Wins',
        ('scissors', 'rock'): 'Computer Wins',
        ('scissors', 'paper'): 'You Win',
    }
    if user == computer:
        return "Draw"
    else:
        return outcomes[(user, computer)]
def main():
    game_components = ['rock', 'paper', 'scissors']
    computer = random.choice(game_components)
    user = get_user_choice()
    print("Computer Chooses:", computer.capitalize())
    result = determine_winner(user, computer)
    print(result)
if __name__ == "__main__":
    main()
