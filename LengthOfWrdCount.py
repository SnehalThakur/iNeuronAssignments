'''
Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
Here 2,3 and 4 are the lengths of the words in the list.
'''

def wordLengthCount(wrds):
    wrdLengthList = []
    for wrd in wrds:
        print("Length of word '{0}' = {1}".format(wrd,len(wrd)))
        wrdLengthList.append(len(wrd))
    return wrdLengthList


lst = ['a','Python','Machine','Learning','data','science','Deep']
print("wrdLengthList-", wordLengthCount(lst))