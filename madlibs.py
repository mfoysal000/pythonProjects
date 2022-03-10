#how to print a string -- a few different ways
#string = 'string'
#print('This is a ' + string + '.')         concatenation(+)
#print('This is a {}.'.format(string))      .format method
#print(f'This is a {string}.')              f string

print('Welcome to madlibs!')

verb1 = input('Enter a present verb: ')
verb2 = input('Enter an infinitive verb: ')
noun1 = input('Enter a noun: ')
pluralNoun = input('Enter a plural noun: ')

madlib = f'''The clock is {verb1.lower()}! Make it quick or else we will {verb2.lower()}! Oh no, it's 
{noun1}. We are doomed now for sure because the {pluralNoun.lower()} shall awake from their slumber.'''

print(madlib)