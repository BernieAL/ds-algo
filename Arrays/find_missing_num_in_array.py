"""

Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array.

Example 1:
Input Format:
 N = 5, array[] = {1,2,4,5}
Result:
 3
Explanation: 
In the given array, number 3 is missing. So, 3 is the answer.

Example 2:
Input Format:
 N = 3, array[] = {1,3}
Result:
 2
Explanation: 
In the given array, number 2 is missing. So, 2 is the answer.

"""


"""
Approach/think through

    objective:
        we're given an array of nums, and asked to find the missing number and return it

    observation:
        we are given integer N
        the array itself is of length n-1
        array contains elements in range of n-1 between 1-n 
        we need to find the number (1-n) that is missing

        ex. 
        say we are given N = 5, and nums = {1,2,4,5}
        
        this means our range of nums is from 1 to 5
        what num is missing from 1 to 5? 
            we can see that is 3

    cases:
        num is present
        num is not present

    evaluation/modeling:

        option 1: expected sum calc - using for loop
            -generate expected nums all nums in range from 1 to N, sum them
            -sum the given elements in nums
            - missing = expected - given 

            o(n) time, o(1) space

            python sum() of nums is o(n)

        option 2: expected sum calc - using first N natural nums formula

            
            we can use formula - sum of first N natural nums to get the expected sum of nums 
                n*(n+1)/2
            
            wheres the indication that we can apply this formula????
                
                problem states we have N numbers in the range of 1 to N
            
                we are given array containing n-1 of these nums

                exactly one num in the range is missing

                the diff between expected_sum and sum of given nums is the missing num

                we are also given an n value

                thats all you need.
                
             o(n) time, o(1) space

             python sum() of nums is o(n)
"""

def missing_num_in_array(n,nums):

    num_sum = sum(nums)
    expected_sum = 1

    for i in range(2,n+1):
        expected_sum+=i

    return expected_sum - num_sum
    
    
print(missing_num_in_array(5,[1,2,4,5]))