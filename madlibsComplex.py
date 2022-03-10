import random

while True:
    print('Welcome to madlibs! Choose your words carefully.')

    adj = input('Please enter an adj: ')
    verb = input('Please enter a verb: ') 
    famousPerson = input('Please enter a famous person: ') 
    place = input('Please enter a place: ') 

    prompt1 = f'''The interstellar spacestation felt {adj} today unlike other days.
The fleet admiral insisted we all {verb} today or we wouldn't be able to get our daily ration.
The admiral reminded me of {famousPerson}--good times. But onwards we go to {place} in this neverending tale.'''

    prompt2 = f'''The creature was so {adj} that it caused me to {verb}.
I reminded myself that if {famousPerson} could do it, so can I! Even in this retched {place}, I will
reach for the stars!'''

    prompt3 = f'''Luke slashed his lightsaber at Darth Vader but Vader was too {adj}.
He knew he had to {verb} but kept fighting regardless because he wanted to be like {famousPerson}.
Luke dreamt of going to {place} but alas he was in a fight for his life with his own kin.'''

    randomMadlib = random.choice([prompt1, prompt2, prompt3])

    print(randomMadlib)

    playAgain = input('Would you like to try again? Y or N?\n')
    if playAgain.lower() == 'y':
        continue
    else:
        print('Goodbye!')
        break
