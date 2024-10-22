print('1. Condition lists: ')
print()
import random

# a. Create a list with 3 members and put random values in it
# random choice - in use True False of

members_list = [random.choice([True, False]) for _ in range(3)]
print(f'This is a list of random booleans: {members_list}')

# b. In one operation, check and print whether the entire list contains only True

# if all([_ > 0 for _ in members_list]):
#     print(f'All is positive on the list: {members_list}')
# else:
#     print(f'All is negative on the list: {members_list}')

print(f'All is positive on the list: {members_list}' if all(_ > 0 for _ in members_list) else f'All is negative on the list: {members_list}')

# c. In one operation, check and print whether the list contains at least one True

print(f' On the list {members_list} all is {all(members_list)}')#all checks if everything in the list is True.

# d. In one operation, check and print whether the entire list contains only False

# if not any(members_list):
#     print('All False')
# else:
#     print('not All False')

print(f' On the list {members_list} all is {not any(members_list)}')#not any checks if everything in the list is False.

# e. In one operation, check and print whether the list contains at least one False

if not all(members_list):
    print('At least 1 False')
else:
    print('0 False')

print(f' On the list {members_list} all is {not all(members_list)}') #not all return True if at least one element is false


# f. Generate a random list of five numbers between 2 and minus 2 (that is, 2, 1, 0 -1, -2)

five_list = [random.randint(-2, 2) for _ in range(5)]
print(f'This is a list of 5 random numbers: {five_list}')

# Use random functions
# g. In one operation, check and print whether the entire list contains only numbers different from 0

print(f'All the numbers on the list are different from 0: {five_list}' if all(_ != 0 for _ in five_list) else f'Not all numbers are diferent from 0: {five_list}')

# h. In one operation, check and print whether the list contains at least one element that is not 0

print(f'At least one number on the list is different from 0: {five_list}' if any(_ != 0 for _ in five_list) else f'Not even one number on the list is diferent from 0: {five_list}')

# i. In one operation, check and print whether the entire list contains only 0

print(f'All the numbers on the list are equal to 0: {five_list}' if all(_ == 0 for _ in five_list) else f'Not all numbers are equal to 0: {five_list}')

# j. In one operation, check and print whether the list contains at least one element that is 0

print(f'At least one number on the list is equal to 0: {five_list}' if any(_ == 0 for _ in five_list) else f'There aren`t any 0 on the list: {five_list}')
