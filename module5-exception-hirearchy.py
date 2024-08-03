import sys

user_name = input('What is your name? ')
if user_name == '':
    print('Empty name? I cannot work with that. I am closing the program. Bye!')
    sys.exit()
print('Hello', user_name)
print('Let us get started...')