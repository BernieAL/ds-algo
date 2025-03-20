
"""


Example 1:
    Input:
        [1,2,4,7,7,5]
    Output:
        Second Smallest : 2
	    Second Largest : 5
    Explanation:
        The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2


"""

"""
Approach
    to find second largest and second smallest, must first find first largest and first smallest

    to find largest and second largest, we need 2 vars, largest and second

    when ever we find new largest, before updating largest, store prev largest as second largest

    same principle applies to smallest

CASES:
    i can be larger than largest
        update second_largest with largest
        update largest with i
    i can be smaller than largest but greater than second_largest
        only update second_largest with i

    i can be smaller than smallest
        update second_smallest with smallest
        update smallest with i
    i can be greater than smallest but smaller than second_smallest
        update second smallest with i
"""


def second_largest_second_smallest(nums):
   largest, second_largest = float('-inf'), float('-inf')
   smallest, second_smallest = float('inf'), float('inf')

   for num in nums:
        #if num greater than largest, update largest
        if num > largest:
            second_largest = num
            largest = num 
        #if num smaller than largest, but greater than second_largest AND is NOT the same value as largest
        elif num > second_largest and num != largest:
            second_largest = num
        
        if num < smallest:
             second_smallest = num
             smallest = num
        elif num < second_smallest and num != smallest:
             second_smallest = num

   return [second_largest,second_smallest]

print(second_largest_second_smallest([1,2,4,7,7,5]))