'''
Write a Python function which takes a character (i.e. a string of length 1) and returns True if
it is a vowel, False otherwise.
'''

def vowelFilter(char):
    if char in ['a','e','i','o','u']:
        return True
    else:
        return False

print("Is 'a' vowel? = ",vowelFilter('a'))
print("Is 'b' vowel? = ",vowelFilter('b'))
print("Is 'c' vowel? = ",vowelFilter('c'))
print("Is 'd' vowel? = ",vowelFilter('d'))
print("Is 'e' vowel? = ",vowelFilter('e'))
