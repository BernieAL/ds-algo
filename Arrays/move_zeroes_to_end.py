"""
https://takeuforward.org/data-structure/move-all-zeros-to-the-end-of-the-array/

Move all Zeros to the end of the array


392

11
In this article we will learn how to solve the most asked coding interview problem: "Move all Zeros to the end of the array"

Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order


Example 1:
Input:
 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output:
 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation:
 All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

Example 2:
Input:
 1,2,0,1,0,4,0
Output:
 1,2,1,4,0,0,0
Explanation:
 All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

"""

"""
Approach

cases

    val is 0 - must move to end
        how, swap with a value, maintaining order
    val is not 0 - stays as is

    brute force
         use addtl array
         copy over non zero elements to temp 
            while iterating, count num of non zero elements
         copy non zero elements back from temp to original 
         append zeroes for remaining positions in original array after non-zero elements

"""
def move_zeros_brute_force(nums):

    temp = [num for num in nums if num != 0] # collect non zero elements 
    zero_count = len(nums) - len(temp) #count zeroes

    #place non zero elements back in original
    #slice nums up to len of temps, set this temp
    nums[:len(temp)] = temp

    #fill remaing space with 0's
    nums[len(temp):] = [0] * zero_count

    return nums




def move_zeros_optimized(nums):
   
    """
 
    The goal here is to move all zeros down to end of array
    we dont want any 0's before non-zero elements.
    
    What this means is we are grouping all non-zero elements to front of array and zero elements to rear of array
        
    
    
    2 ptrs to avoid need for addtl array and does operation in-place
        1 ptr to traverse the array
        1 ptr will be used to track where next non-zero element will go - insert_pos (ip)

        when iterator ptr encounters non-zero, we swap the value of insert_pos with iterator_ptr

    we dont need to add zeroes in, because we are swapping elements around. 
    all zeros automatically move toward the end as non-zero elements are moved up


    input cases:
        [1,0]  -> needs nothing
        [0,1] -> need to swap, need to find 0 to find set insertion point for non zero element swap
        [0,0] -> nothing
        [1,1] -> no zeros
        [1,2,0,4] -> needs swap, need to find 0 to set insertion point for non zero element swap
        [] -> empty array, return nums


    Claude docstring
        Move all zeros in the array to the end while maintaining the relative order of non-zero elements.
    
        Algorithm explanation:
        1. Find the first zero in the array - this becomes our first insertion point
        2. For each non-zero element after the first zero:
        - Swap it with the current zero position (bringing non-zeros forward)
        - Advance the insertion pointer to the next zero position
        
        The key insight is that after each swap, a non-zero element occupies the previous zero position,
        so we need to find the next available zero to use as the new insertion point.
        
        Time complexity: O(n) - we process each element at most twice
        Space complexity: O(1) - we modify the array in-place using only pointers
        
        Args:
            nums: List of integers
            
        Returns:
            The modified list with zeros moved to the end

            
    """


    #EDGE CASE empty check
    #necessary because nums could be empty, if so, just return nums
    if not nums:
        return nums
    
    #FINDING POS OF FIRST 0 - setting this as first insertion point
    # find position of first 0,  this will be used as first place to insert a non-zero
    #without knowing position of first 0, we dont cant swap 0 with non-zero element
    #necessary because we are swapping 0's with non-zeros, pushing 0's towards back of array
    i = 0
    while i < len(nums) and nums[i] != 0:
        i+=1

    #EDGE CASE - no zeroes in array
    # if our i reaches end of nums and havent found 0, return the original array -> theres no zeroes
    # if no zeros found, return original array
    if i == len(nums):
        return nums
    
    #FINDING NON ZERO ELEMENTS 
    # look for non-zero elements that occur after first zero
    for j in range(i+1,len(nums)):

        #if value is non-zero, we found a value that occurs AFTER 0, we must swap to push 0 down
        if nums[j] != 0:
            nums[j], nums[ip] = nums[ip],nums[j]

            #SEARCH FOR NEXT 0
            # move ip forward until we hit a 0 again
            #this is necessary because when we advance ip, it could land on non-zero
            #and we cant insert on a non-zero element's place, so we must find next 0
            #once next 0 is found, we can proceed with next iteration of for loop
            ip +=1
            while ip < len(nums) and nums[ip] != 0:
                ip+=1

            #if our insertion_pointer - is at end of nums, we have no more zeros
            # if no more zeros, we are done
            if ip == len(nums):
                break

    return nums
    




    #check if array is empty
    #find first 0, this is our first insertion point for non zero element
    for i in range(len(nums)):
        if nums[i] == 0:
            ip = i
            break
    
    #now look for non zero elements, swap to ip position
    #once we swap, go on to look for next 0 which is next ip
    for j in range(i+1,len(nums)):
        if nums[j] != 0:
            nums[j],nums[ip] = nums[ip],nums[j]

            #move ip forward until we hit a 0 again
            # cases for ip, it can be non zero or zero
            # if non zero, this is no good for us, we need a 0
            # move it forward til we get a 0, then resume the for loop    
            while nums[ip] != 0:
                ip+=1
        