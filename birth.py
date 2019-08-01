# Birthday paradox done in python
# Program by Eren Sulutas

import random

subjects = 100
birthday_list = []
matching = False

for i in range(subjects):
    birthday = random.randint(0, 365)

    if birthday in birthday_list:
        print("\nMatching birthdays found at {} subjects\n".format(i))
        matching = True
        break
    else:
        birthday_list.append(birthday)

if not matching:
    print("\nNo matching birthdays found with {} subjects\n".format(subjects))
