import random

def guess(x):
    randomNumber = random.randint(1, x)
    guess = 0

    while guess != randomNumber:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < randomNumber:
            print("Sorry!, guess again. Too Low.")
        elif guess > randomNumber:
            print("Sorry!, guess again. Too High.")
    print(f"Yay, congrats. You have guessed the number {randomNumber} correctly!!!")
  
def computerGuess(x):
    low = 1
    high = x

    feedback = ''
    while feedback != 'c':
        if low != high:
           guess = random.randint(low, high)
        else:
           guess = low
        feedback = input(f"Is {guess} too High (H), too Low(L), or Correct(C) ??? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"yay,The computer guessed your number,{guess},correctly")


guess(10)
