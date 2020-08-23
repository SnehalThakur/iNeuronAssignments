# Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()
import functools
list1 = [10,20,30,40,50]

# Using build-in reduce()
print("Result of build-in reduce() for list of number",list1," = ",functools.reduce(lambda x,y: x+y, list1))

# Using custom reduce function myreduce()
def add(num1, num2):
    return num1+num2

def myReduce(func, nums):
    first = nums[0]
    for i in range(1,len(nums)):
        first=func(first,nums[i])
    return first

print("Result of custom myreduce() for list of number",list1," = ",myReduce(add, list1))
