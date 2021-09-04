#!/usr/bin/env python3

import random, pyperclip, string, secrets

password = ''
password = password + secrets.choice(string.digits)
password = password + secrets.choice(string.punctuation)
password = password + secrets.choice(string.punctuation)

for letter in range(9):
    random_letters = secrets.choice(string.ascii_letters)
    password = password + random_letters

password_list = list(password)
random.shuffle(password_list)
new_password = ''.join(password_list)

pyperclip.copy(new_password)
print('Password has been copied to the clipboard')