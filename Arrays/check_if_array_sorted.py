"""

Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

Note: Two consecutive equal values are considered to be sorted.

Example 1:
    Input:
        N = 5, array[] = {1,2,3,4,5}
    Output: 
        True.
    Explanation:
        The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.
"""

"""
Approach

    starting from first element 
        check if next element greater than prev 

        if next element is not greater than prev, return false

        if we havent thrown false, and we've gone through all elements,
        return true

"""

def check_sorted(nums):
    prev = nums[0]

    for i in range(1,len(nums)):
        
        
        #if next num less than prev
        if nums[i] < prev:
            return False
        
        #else update prev with curr num
        prev = nums[i]

    return True
        


print(check_sorted([1,2,3,3,4]))