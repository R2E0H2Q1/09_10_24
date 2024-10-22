print('2. Basics - Strings:')
print()

#  will generate a (one) string of your full name and city of residence. Make sure there is a space between the names
name: str = 'Reuben'
lname: str = 'Herrera'
residence: str = 'Kfar Saba'

details = f'{name} {lname} resides in {residence}!'
print(details)
print()

# a. Print the length of the string. Hint len

print(f'The length of the string details is: {len(details)} characters.')
print()

# b. Print the entire string in uppercase. hint upper

print(f'This is an example of UPPERCASE format: {details.upper()}.')
print()

# c. Print the entire string in lowercase. Hint lower

print(f'This is an example of lowercase format: {details.lower()}.')
print()

# d. Check if the string starts with your first name. hint startswith

print(f'This is an example of the use of "startswith", for this particular case the result is: {details.startswith(name)}.')
#checks if a string starts with a certain substring
print()

# e. Check if the string ends in your city of residence. Hint endswith

endcheck = details.endswith(residence)
print(f'This is an example of the use of "endswith", for this particular case the result is: {endcheck}.')
print()

# f. Extract the string into a list containing your first name, last name, city of residence. hint split

details_list = details.split()
print(f'Example of the string details in format list: {details_list}')
print()

# g. Turn spaces into asterisks. Hint replace. Then - unpack the new string again

replace_string = details.replace(" ", "*")
print(f'The new string with * instead of empty spaces: {replace_string}')
print()

# to the list (as in the previous section)

second_list = replace_string.split()
print(f'Example of the string replace in format list: {second_list}')
print()

# h. Print the string in the center of 50 characters, wrapped in the "=" character. Hint center

print(replace_string.center(50, '='))
print()

# i. Print the string from the 4th character to the end

f4tend_string = replace_string[3:]
print(f'The string replace_string starting from character 4 until the end: {f4tend_string}')
print()

# j. Print the string from the beginning to the 4th character (inclusive)

f0t4_string = replace_string[:5]
print(f'The string replace_string starting from character 0 until character 4: {f0t4_string}')
print()

# k. Print all even characters in a string

even_string = replace_string[::2]
print(f'The string of even characters from "replace_string": {even_string}')
print()

# l. Make sure each word in the string starts with a capital letter. Hint title

ttle_string = replace_string.title()
print(f'This is an example of format title on a string: {ttle_string} ')