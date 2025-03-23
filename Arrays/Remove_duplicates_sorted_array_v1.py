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


    goal: remove all duplicate elements

    constraints:
        nums must remain in same order
        array length must remain unchanged

    
    BF:
        how to mark duplicates?
            mark as seen using hashmap or set rather
        
        cases:
            if val is NOT in set -> its a duplicate
                use while loop to find the next element thats not the same as curr, swap them
                this pushes the duplicate to the back

            reason for DOING NOT in SET is because duplicates will ofcourse be in the set
            so mark a value as seen, we pop from set
            this way, if we encounter the val again, we will see its a dupe, and we should treat is a dupe
            meaning, use while loop to find next element that is different from this curr element and is still in the set, meaning its not a duplicate
                that looks like:  
                    
                    while i != i+1 and i not in num_set:
                        i+=1
                    non_dupe = i
                    this would leave us on a non dupe value ready for next for loop iteration

            can maintain a pointer that acts as unique sequence builder
            it maintains the index pos of where to place the next non duplicate

        
        num_set = set(nums)

        for num in nums:
            #mark seen by removing from num_set

            if num in num_set:
                num_set.remove(num)

        non_dupe = 0
        for i in range(len(nums)):
            
            j = i + 1
            while j == j + 1 and j not in num_set:
                nums[j+1] = '_'
                j+=1

            nums[i],nums[j] = nums[j], nums[i]

        #get # of elements that arent '_'
        return len([i for i in nums if i != '_'])                
            
            


                 

"""

"""
Didnt finish in 25 mins first try (3/21/25)


gave 30 more mins for this writeup

we want to remove duplicates
how to flag something as a duplicate?

brute force:
    make a set from nums
    to mark a value as a duplicate, we will remove it from the set
        if a value is missing from the set, its already been marked a duplicate
    
    after we know whats a duplicate and what isnt,
    find the first non-duplicate in the array, 
    this will be the start of our unique list, we set a pointer as first NON duplicate + 1, the next pos where one will go

    we then go through nums again - this time we are looking for the next non duplicate to insert in unique sequence
    to do this
        set iterator to ip+1
        while iterator is equal to next element and not in set, iterator   
            cases:
                can have 2 identical values adjacent
                or we can have 2 different values but both are already ruled duplicates using set

        when while ends, ip will be at next location where we should put next non duplicate

"""

def remove_dup_sorted_array(nums):

    num_set = set(nums)
    print(num_set)
    print(nums)
    #determine what is a duplicate using set
    for i in range(len(nums)):

        #for each in nums, mark a number as seen by removing it from the set
        #the reason for this is, if we encounter a number that is already missing from the set,
        #this means encountered a duplicate value - we mark the index containing the duplicate as 'x'


        #if this num has been removed from num_set already, we encountered a duplicate
        #overwrite the val at this index with 'x'
        if nums[i] not in num_set:
            nums[i] = 'x'
        #if this is the first time we this num, remove it from the set to mark as seen
        
        elif nums[i] in num_set:
            num_set.remove(nums[i])

    
    #set before -> (1,2,3,4)  
    #set after -> empty set
    #should now have -> [1,x,x,2,x,3,x,x,x,4,x]

    
    
    #INSERTION POINTER - FIRST NON X + 1
    #get the position of the first non-x element
    #set insert_pointer to this index + 1
    #insertion of next non-x element will occur at this index + 1
    j = 0
    while j < len(nums) and nums[j] != 'x':
        j+=1
    
    ip = j
    
    #SWAP - X with non X (duplicate with non duplicate)
    #from insertion point onward, swap x's with non x.
    for i in range(ip+1,len(nums)):

        #if we encounter a x
        if nums[i] != 'x':
            
            #put non duplicate value at insertion_point
            nums[ip],nums[i] = nums[i],nums[ip]

            #increment insertion pointer to next spot for next non x value
            ip+=1

            #SEARCH FOR NEXT insertion_point -> search for next 'x' 
            #when we advance ip, it could fall on non-x value and we dont want that - cant insert on non 'x'
            #once next x is found, we can proceed with next iteration of for loop

            while ip < len(nums) and nums[ip] != 'x':
                ip+=1

            if ip == len(nums):
                break
        
    
    return nums


print(remove_dup_sorted_array([1,1,1,2,2,3,3,3,3,4,4]))#