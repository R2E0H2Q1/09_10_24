print('3. Strings - Part 2:')
print()

# a. Remove the spaces from both sides of the following string: " fun-day "

spaced_string = ' Fun-day '
print(f'This is a string with 2 spaces: {spaced_string}')

fd_string = spaced_string.replace(' ', '')
print(f'The spaces were removed: {fd_string}')
print()

# b. Check if the string "hello" contains only letters. Hint isalpha

hello_str = 'hello'
checkup = hello_str.isalpha()# #check if all the characters in a string are alphabetic
print(f'Example of use of "isalpha", in this example the result is: {checkup} ')
print()

# c. Check if the string "777" contains only numbers. hint isdigit

nums_str = '777'
checknums = nums_str.isdigit()# #check if all the characters in a string are numbers
print(f'Example of use of "isdigit", in this example the result is: {checknums} ')
print()

# d. Check if the string " " contains only spaces. Hint isspace

space_str = ' '
checkspace = space_str.isspace()
print(f'Example of use of "isspace", in this example the result is: {checkspace} ')
print()

# e. For the list ['A','J','N','I','N']. Create one string from it. Hint join

joined_list = ['A','J','N','I','N']
new_string = ' '.join(joined_list)
print(f'This is an example of the use of method "join": {new_string} ')
print()

# f. For the same list - create one string with '*' between the characters. A*J*N*I*N. Hint join

second_str = '*'.join(joined_list)
print(f'This is an example of the use of method "join": {second_str} ')
print()

# g. Ignoring upper and lower case letters: check if the letter e appears in the word hELLo. Hint: lower

lettercheck = 'hELLo'
object = 'e'

if object in lettercheck:
    print(f' The letter {object} is present in the string!')

else:
    print(f' The letter {object} is present in the string!')