import random
from art import *
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess =int(input("new no:"))

    if guess > 0:
        if guess > to_be_guessed:
            print('not this time nerd think SMALL')
        elif guess < to_be_guessed:
            print('y ?think big kiddo')
    else:
        print('HAH WHAT ELSE YOU COULD HAVE DONE LOOSER')
        break
else:
    print('big brainzz nerd')
    tprint("you win","rnd-xlarge")


    

    
    
    
    
