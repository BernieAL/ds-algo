# https://takeuforward.org/data-structure/find-the-largest-element-in-an-array/


"""


    Example 1:
    Input:
        arr[] = {2,5,1,3,0};
    Output:
        5
    Explanation:
        5 is the largest element in the array. 


    Approach:
        max_seen to track max value seen overall

        use for loop to go through all vals
            for each val compare to max_seen, 
                if greater than, update max_seen

        this is o(n)

"""

def largest_in_array(nums:int):
    max_seen = float('-inf')
    
    for num in nums:
        if num > max_seen:
            max_seen = num  

    return max_seen

print(largest_in_array([2,5,1,3,0]))