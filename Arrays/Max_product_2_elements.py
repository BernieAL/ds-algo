"""
Chatgpt generated problem


Given array of integers, find maximum product of any 2 elements
[1,2,3,4]
"""

"""
Approach

How to multiply each 2 numbers
    1
        1*2, 1*3, 1*4
    2
        2*3, 2*4
    3
        3*4
    4
        -

"""

def find_max_product(nums):
    
    max_prod = float('-inf')

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            prod = nums[i] * nums[j]
            max_prod = max(max_prod,prod)
    return max(max_prod,local_max)
print(find_max_product([1,2,3,4]))