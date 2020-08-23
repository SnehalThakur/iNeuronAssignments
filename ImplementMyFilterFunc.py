# Write a Python program to implement your own myfilter() function which works exactly
# like Python's built-in function filter()

list1 = [100, 200, 300, 400, 500, 600]

#Using build-in filter()
print("Result of built-in filter() for number > 300 list", list1, "=", list(filter(lambda x : x > 300, list1)))



def findGreaterNum(num):
    if num > 300:
        return num
    else:
        pass

def myFilter(func, nums):
    filteredList = []
    for i in range(1, len(nums)):
        if func(nums[i]):
            filteredList.append(func(nums[i]))
    return filteredList

print("Result of custom myfilter() for number > 300 list", list1, "=", myFilter(findGreaterNum,list1))