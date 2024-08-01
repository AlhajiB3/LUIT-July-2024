print('Hello', 'How are you?', end='.', sep='-')

def print_letter_count(text='This is the default strong to search', letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

# Call the function with a text string; the letter defaults to 'a'
print_letter_count('How many letter a are here?')

print_letter_count()
