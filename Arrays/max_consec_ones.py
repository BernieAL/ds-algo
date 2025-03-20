"""

Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.


Example 1:

    Input: prices = {1, 1, 0, 1, 1, 1}

    Output: 3

    Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.

    Input: prices = {1, 0, 1, 1, 0, 1} 

    Output: 2

    Explanation: There are two consecutive 1's in the array. 


"""

"""
approach

    cases:
       if val is 1 
            increment count
       if val is 0
            start count over
       compare to max
       
       return max

"""

def max_consec_ones(nums):
    
    curr_count = 0
    max_count = 0

    for num in nums:
        
        if num == 1:
            #increment curr_count
            curr_count +=1
        if num == 0:
            #reset to 0
            curr_count = 0

        #update max_count before resetting curr_count
        max_count = max(max_count,curr_count)
    
    return max_count





print(max_consec_ones([1,0,1,1,0,1]))