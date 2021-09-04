import random

computer = ['rock', 'paper', 'scissors']
computer = random.choice(computer)
human = (input('Pick one: rock, paper, or scissors: ')).lower()

# rock wins over scissors
# paper wins over rock
# scissors wins over paper
print('COMPUTER picks:', computer)
print('YOU pick', human)
print()

if computer == 'rock' and human == 'scissors':
    print('Computer WINS!')
elif computer == 'paper' and human == 'rock':
    print('Computer WINS!')
elif computer == 'scissors' and human == 'paper':
    print('Computer WINS!')
elif computer == human:
    print("It's a TIE!")
else:
    print('Human WINS!')