"""
Given an array arr. The task is to find the largest element in the given array. 

Examples: 

Input: arr[] = [10, 20, 4]
Output: 20
Explanation: Among 10, 20 and 4, 20 is the largest. 


Input: arr[] = [20, 10, 20, 4, 100]
Output: 100


Try it on GfG Practice
"""
#qustions 1
def Large_Element(arr):
    max = arr[0]
    for i in range(len(arr)):
        if arr[i]>max:
            max = arr[i]
    return max
arr=[10, 20, 4]
result = Large_Element(arr)
print(result)

# Qustions 2
def Big_Element(Nums):
    max = Nums[0]
    for i in range(len(Nums)):
        if Nums[i]>max:
            max = Nums[i]
    return max
Nums = [20, 10, 20, 4, 100]
Big = Big_Element(Nums)
print(Big)

# Finde the smolest element in this array

def Finde_Smoll(Num):
    min = Num[0]
    for i in range(len(Num)):
        if Num[i]<=min:
            min= Num[i]
    return min
Num= [20, 10, 20, 4, 100]
Smoll = Finde_Smoll(Num)
print(Smoll)
