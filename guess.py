import random

playing = True

num = str(random.randint(0,9))
while playing:
    guess = input("Guess a number form 0 to 9: ")
    if guess == num:
        print("You guessed right")
        playing = False
    else:
        print("galat tukka lageya , fir se koshish karo")