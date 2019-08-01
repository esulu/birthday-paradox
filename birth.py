import random

subjects = 10
birthday_list = []

for i in range(subjects):
    birthday = random.randint(366)

    if birthday in birthday_list:
        print("Matching birthdays found with {} subjects".format(i))

    
