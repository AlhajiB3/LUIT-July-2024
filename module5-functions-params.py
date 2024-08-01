def get_average(input_numbers):
    sum = 0.0 
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)

    print(average)

get_average([5.0, 3.5, 7.8, 9.9, 10.0])

def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)

# Call the function with the desired text and letter
print_letter_count('Welcome', 'e')

print_letter_count('Anything is possible, All things are possible.', 'a')

print_letter_count('e', 'Welcome')