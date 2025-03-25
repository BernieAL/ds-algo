"""
Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

Example 1:
Input Format:
 arr[] = {2,2,1}
Result:
 1
Explanation:
 In this array, only the element 1 appear once and so it is the answer.

Example 2:
Input Format:
 arr[] = {4,1,2,1,2}
Result:
 4
Explanation:
 In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.


"""
"""
Approach/think through

    objective: 
        from array of non-empty intergers, 
        every element appears twice except for one, find the single element that appears only ONE TIME

    questions:
        is input sorted? - doesnt matter

    observations:
        every element appears twice except for one

        specific mention of every element appearing TWICE
        could be oppurtunity for XOR bitwise operation properties

        a ^ a = 0
        a ^ 0 = a
            


    cases:
        a num is a duplicate
        a num is not a duplicate
    
    evaluation/modeling:

        need to track values we've seen
        
        brute force - counting occurences using hashmap
            use hashmap, where k is a num, v is occurence count
            
            1st pass puts all nums and hashmap and increments their counts

            2nd pass goes through hashmap and returns the value
            with only 1 occurence

            o(n), o(n) space

        optimized using - xor operation properties

            if we XOR all nums in the array, the duplicate nums cancel out to 0, and this leaves us with the only num that wasnt canceled out.

            result = 0
            for num in nums:
                result ^= num
            return result
            
            Ex.
                4,1,2,1,2

            res = 0
                
                num = 4
                    res ^= 4 -> 4

                res=4
                num = 1
                    res ^= 1 -> 4^1 = 5
                
                res = 5
                num = 2
                    res ^= 2 -> 5^2 = 7

                



"""


def appear_once_appear_twice(nums):

    res = 0
    
    #for each num, xor with res - this will xor all values
    for num in nums:
        res ^= num
    
    return res
   

print(appear_once_appear_twice([4,1,2,1,2]))