"""

READ ME

I made my own version of the problem accidentally - I was only supposed to return the number of unique elements in the array
Instead, I returned the array with duplicates removed and pushed to the back.





https://takeuforward.org/data-structure/remove-duplicates-in-place-from-sorted-array/

Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.

If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.

Note: Return k after placing the final result in the first k slots of the array.

Examples
Example 1:
Input:
 arr[1,1,2,2,2,3,3]

Output:
 arr[1,2,3,_,_,_,_]

Explanation:
 Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.

Example 2:
Input:
 arr[1,1,1,2,2,3,3,3,3,4,4]

Output:
 arr[1,2,3,4,_,_,_,_,_,_,_]

Explanation:
 Total number of unique elements are 4, i.e[1,2,3,4] and Therefore return 4 after assigning [1,2,3,4] in the beginning of the array."
"""

"""
Approach/think through

    objective: return the total number of unique elements
    
    observation:
        were being asked to perform counting operation
        might be oppurtunity to use 2 ptrs here with an addtl pointer
        for maintaining the count of unique values instead of an addtl datastructure

        we can check nums in-place and mark in-place

    input given:  arr[1,1,1,2,2,3,3,3,3,4,4]

    simple case:
        [1,1,1,2,2,3]

    cases:
       1) a number can be unique
       2) a number can be a duplicate

    evaluation
        how to check if a num is a duplicate?
            need to track what we've seen for far
            what are common patterns to track what we've seen
                can use hashmap
                    K:v pair, k is num, v can be 0
                    if a val is already in dict, current val we are on is a dupe
                    mark value at this index with x
                    if val not already in dict,
                        add it to dict

                can use set
                    make a set from nums
                    to mark a value as seen, delete it from set
                        increment unique count
                    to check if a value is a duplicate, we see if its missing from set
                        if missing from set, mark index with x
                        

                can we do it with 2 ptrs, checking in-place?
                    if we can gurantee the input is sorted
                    or go on to sort the input ourself,
                    
                    set ptr A to front of list
                    set ptr B to A+1
                    set unique_counter to 1 because of element at ptr A

                    when B encounters a value that is different from A,
                    we increment unique_count, set A to index of B,
                    then set B to B+1, then repeat the check


"""

def Remove_duplicate_sorted_array_v2(nums):

    #ptr for tracking unique elements only
    a = 0
    #iterator ptr for comparing all elements to current unique element 'a'
    b = 1
    unique_count = 1 #first element always counted as unique

    
    #while b in bounds of array
    while b < len(nums):
        
        #if b found a value different from what A points to
        if nums[b] != nums[a]:
            #move a to b position to mark new unique element found
            a = b
            unique_count += 1

        #advance b to check next element
        b += 1

    return unique_count

print(Remove_duplicate_sorted_array_v2([1,1,1,2,2,3,3,3,3,4,4]))