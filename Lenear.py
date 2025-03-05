"""
Input: arr[] = [1, 2, 3, 4], x = 3
Output: 2
Explanation: There is one test case with array as [1, 2, 3 4] and element to be searched as 3. Since 3 is present at index 2, the output is 2.


Input: arr[] = [10, 8, 30, 4, 5], x = 5
Output: 4
Explanation: For array [1, 2, 3, 4, 5], the element to be searched is 5 and it is at index 4. So, the output is 4.


Input: arr[] = [10, 8, 30], x = 6
Output: -1
Explanation: The element to be searched is 6 and its not present, so we return -1.


"""
# first Problem
"""
def FindeElement(arr,X):
    for i in range(len(arr)):
        if arr[i]==X:
            return i
    return -1
if __name__ =="__main__":
    arr= [1, 2, 3, 4]
    X = 3
    result = FindeElement(arr,X)
if result ==-1:
    print("Elemente is Not Found")
else:
    print(f"Elemente is persernt in  index {result}")
"""

#qustion 2
def check_element(arr,X):
    for i in range(len(arr)):
        if arr[i]==X:
            return i
    return -1
if __name__=="__main__":
  arr =[10, 8, 30, 4, 5]
  X = 5
  results = check_element(arr,X)
if results ==-1:
    print("Not Found")
else:
    print(results)


#Qustions 3
def Qustions(Nums,X):
    for i in range(len(Nums)):
        if Nums[i]==X:
            return i
    return-1
Nums = [10, 8, 30]
X = 6
Element = Qustions(Nums,X)
print(Element)