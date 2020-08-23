# Write a function filter_long_words() that takes a list of words and an integer n and returns
# the list of words that are longer than n.


def filter_long_words(listOfWords, length):
    filteredList = []
    for i in listOfWords:
        if len(i)>length:
            filteredList.append(i)

    return filteredList


lst = ['Python','Machine','Learning','data','science','Deep']
filteredWrds = filter_long_words(lst,4)
print(filteredWrds)