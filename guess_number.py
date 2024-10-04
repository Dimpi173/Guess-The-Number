import random
import logo
print(logo.logo)
'''random_number = random.randint(1, 100)
#print(random_number)


print("-------Welocome to the guessing game-------")
print("Let me think a number between 1 to 100")
level = input("Choose level of difficulty... Type 'easy' or 'hard'").lower()
if level == "easy":
  attempts = 10
elif level == "hard":
  attempts = 5

# easy 10 attemps, hard 5 attemps
i = attempts
while i >= 0:
  if i == 0:
    print("You lose")
    break
  else:
    print("Guess Again")
  print(f"You have {i} attempts left")
  user_guess = int(input("Make a guess: "))
  if user_guess == random_number:
    print(f"You got it! The answer was {random_number}")
    print(f"You guess it in {i} attempts")
    break
  elif user_guess >random_number:
    print("Your Guess is too high")
    #print("Guess again")
    i -= 1
  elif user_guess < random_number:
    print("Your Guess is too low")
    #print("Guess again")
    i -= 1
'''

EASY_level = 10
HARD_level = 5


def set_level(level):
    if level == "easy":
        return EASY_level
    elif level == "hard":
        return HARD_level
    else:
        print(f"You have entered {level} which is not valid")
        return set_level(input("Choose level of difficulty... Type 'easy' or 'hard'").lower())


def check_number(user_guess, random_number, attempts):
  
    if user_guess < random_number:
        print("Your guess is too low")
        return attempts - 1
    elif user_guess > random_number:
        print("Your guess is to high")
        return attempts-1
    else:
        print(f"Your guess is right... The anser is {random_number}")


def game():
    print("Let me think a number between 1 to 100")
    random_number = random.randint(1, 100)
    level = input("Choose level of difficulty... Type 'easy' or 'hard' ").lower()
    attempts = set_level(level=level)
    user_guess = 0
    while user_guess != random_number:
        print(f"You have {attempts} remaining to guess the number")
        user_guess = int(input("Guss a number: "))
        attempts = check_number(user_guess, random_number, attempts)
        if attempts == 0:
            print("Your out of guesses..... You lose")
            return
        elif user_guess != random_number:
            print("Guess again")


game()
