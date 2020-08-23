'''
Write a Python program to reverse a word after accepting the input from the user.
Input word: ineuron
Output: norueni
'''

word = input("Enter a word")
print('Input word = ',word)
# Reverse a word Mtd 1
print('Reversed word is "{}"'.format("".join(reversed(word))))

#Reverse a wrd Mtd2
print('Reversed word is "{}"'.format(word[::-1]))