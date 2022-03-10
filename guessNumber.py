#Guessing number game
import random

while 1:
    choice = int(input('''Welcome to the guessing game! Please choose a game type:
1) Guess the number 2) Let the computer guess your number\n'''))



    def guess(boundary):
        '''Game 1'''
        print(f'Guess a number between 1 and {boundary}')
        secretNumber = random.randint(1,boundary)
        guess = 0
        tries = 0
        while(guess != secretNumber):
            tries += 1
            guess = int(input())
            if guess > secretNumber:
                print('Hey, that is too high')
            elif guess < secretNumber:
                print('Hey, that is too low')

        print(f'You guessed {secretNumber} correctly! It took you {tries} tries!')

    if choice == 1:
        print('Pick a maximum boundary for a random number.')
        guess(int(input()))


    def computerGuess(boundary):
        '''Game 2'''
        
        low = 1
        high = boundary
        userFeedback = ''
        tries = 0 

        while(userFeedback != 'c'):
            tries = tries + 1

            if low != high:
                compGuess = random.randint(low, high)
            else:
                compGuess = low 
            
            userFeedback = input(f'Is {compGuess} too high (H), too low (L), or correct (C)?\n')
            if userFeedback.lower() == 'l':
                low = compGuess + 1 
            elif userFeedback.lower() == 'h':
                high = compGuess - 1 


        print(f"I guessed it correct, didn't I!? And it only took me {tries} tries!")

    if choice == 2:
        print('Please pick a maximum boundary for a random number for me to guess.')
        computerGuess(int(input()))
    


    restart = input('Do you wish to continue (Y/N)\n')
    if restart.lower() == 'y':
        continue
    else:
        print('Goodbye!')
        break

