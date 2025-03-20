"""

Find 2 numbers that add up to target

"""


"""
Approach
    calc complement -> target - nums[i]
    check if complement is in dict,
        if yes, that means curr num and complement sum to target as pair
        if no, store current num and its index in dictionary

    
"""
def two_sum(nums,target):
    my_dict = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in my_dict:
            return [nums[i],complement]
        my_dict[nums[i]] = nums[i]

    return None

print(two_sum([2,7,11,15],9))
