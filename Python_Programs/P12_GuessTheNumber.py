'''
Write a Python program that implements a guessing game. The program should:
Generate a random number: The program should use the random library to generate a secret number between 1 and 100.
Get user input: The program should prompt the user to guess the number and use a loop to ensure the user enters a valid integer within the range of 1 to 100.
Provide hints:
The program should check the user's guess and provide hints like "Too high" or "Too low" to guide the user towards the correct answer.
Track attempts: The program should keep track of the number of guesses the user makes.
Calculate score: The program should calculate the user's score based on the number of attempts, with a higher score for fewer attempts (e.g., 100 points divided by the number of attempts).
Display results: The program should display a message indicating if the user guessed the correct number.
Show score: The program should display the user's score rounded to two decimal places.
'''
#Simple Code
'''
import random
a = random.randint(1,100)
score = 100
attempt = 1
b = int(input("I have a number between 1 to 100. Can you guess the number: "))
while b != a:
    attempt += 1
    print("Your Guess is wrong")
    score/=attempt
    if b > a:
        print("Too high")
    else:
        print("Too Low")
    b = int(input("Try Again\n"))
if b == a:
    print("You Guessed it right!")
    print("Score: ",score)
'''
import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    max_score = 100

    print("I have a number between 1 to 100. Can you guess the number?")

    while True:
        user_guess = get_user_input()
        attempts += 1

        if user_guess == secret_number:
            print("You Guessed it right!")
            print("Attempts:", attempts)
            calculate_and_display_score(attempts, max_score)
            break
        else:
            print("Your guess is wrong.")
            provide_hint(user_guess, secret_number)

def get_user_input():
    while True:
        try:
            user_input = int(input("Enter your guess: "))
            if 1 <= user_input <= 100:
                return user_input
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def provide_hint(user_guess, secret_number):
    if user_guess > secret_number:
        print("Too high.")
    else:
        print("Too low.")

def calculate_and_display_score(attempts, max_score):
    score = max_score / attempts
    print("Score:", round(score, 2))

if __name__ == "__main__":
    guess_the_number()