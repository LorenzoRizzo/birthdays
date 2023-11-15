birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}

def print_birthdays():
    print('Welcome to the birthday dictionary. We know the birthdays of these people:')
    for name in birthdays:
        print(name)

def return_birthday(name):
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))

'''
 The goal of this module is to elevate our python and git abilities to a new level. 
'''
 birthdays = {
     'Albert Einstein': '03/14/1879',
     'Benjamin Franklin': '01/17/1706',
     'Ada Lovelace': '12/10/1815',
     'Donald Trump': '06/14/1946',
     'Rowan Atkinson': '01/6/1955'}
def print_birthdays():
'''This function prints the name of the person if present in the data'''
print('Welcome to the birthday dictionary:') for name in birthdays:
print(name)
def return_birthday(name): '''This function prints the birthday of a person present in the data given the name of the person''' if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))