import random, string, time

# User input and check if input is a number and between 1 and 40.
picked_numbers = []
while len(picked_numbers) < 6:
    number = input('Enter your selected numbers between 1-40. Ex: 14:\n')
    if number.isdigit:
        if int(number) <= 40 or int(number) >= 1:
            picked_numbers.append(int(number))
        else:
            print('The number is either more than 40 or less than 1')
    else:
        print('Please pick numbers between 1 and 40.')
print('You picked the following numbers:',picked_numbers, '\n')

# Generate winning lotto numbers.
winning_numbers = random.sample(range(1,40), 6)
print('Here are the winning numbers for tonights draw!')
for winning_number in winning_numbers:
    time.sleep(2.5)
    print(winning_number)

time.sleep(1)
print('The winning numbers are:', winning_numbers, '\n')

# Compare picked numbers to winning numbers
count = 0
for number in picked_numbers:
    time.sleep(1)
    if number in winning_numbers:
        print(number, 'has been drawn.')
        count = count + 1
print(count, 'of your numbers have been drawn.')