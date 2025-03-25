"""

Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

The union of two arrays can be defined as the common and distinct elements in the two arrays.NOTE: Elements in the union should be in ascending order.

Example 1:
Input:

n = 5,m = 5.
arr1[] = {1,2,3,4,5}  
arr2[] = {2,3,4,4,5}
Output:

 {1,2,3,4,5}

Explanation: 

    Common Elements in arr1 and arr2  are:  2,3,4,5
    Distnict Elements in arr1 are : 1
    Distnict Elemennts in arr2 are : No distinct elements.
    Union of arr1 and arr2 is {1,2,3,4,5} 

Example 2:
Input:

    n = 10,m = 7.
    arr1[] = {1,2,3,4,5,6,7,8,9,10}
    arr2[] = {2,3,4,4,5,11,12}
    Output:
    {1,2,3,4,5,6,7,8,9,10,11,12}
Explanation:
 
    Common Elements in arr1 and arr2  are:  2,3,4,5
    Distnict Elements in arr1 are : 1,6,7,8,9,10
    Distnict Elements in arr2 are : 11,12
    Union of arr1 and arr2 is {1,2,3,4,5,6,7,8,9,10,11,12} 


"""


"""

Approach/Think through:


    # Array Union Problem: Study Notes

    ## Problem Understanding
    - **Key Insight**: Find the union of two sorted arrays with no duplicates in the result
    - **Expected Output**: A sorted array containing all unique elements from both input arrays

    ## Input Data Properties
    - **Sorted Arrays**: Both input arrays are already in ascending order
    - **Duplicates**: An individual array can contain duplicates within itself
    - **Common Elements**: Both arrays can have overlapping elements
    - **Array Sizes**: Arrays can have different lengths
    - **Edge Cases**: Consider empty arrays and boundary conditions

    ## Approach Analysis
    ### Strategy: Merge-Sort Style Approach
    Use a two-pointer technique to merge the arrays while handling duplicates

    ### Example Cases to Consider:
    1. **Basic Case (No Overlap)**: [1,2,3] and [4,5,6]
    - Compare elements, add the smaller one to result, advance pointer

    2. **Overlap Case**: [1,2,3] and [2,3,4]
    - Need to avoid adding duplicates when elements are common
    - When elements are equal, add only once and advance both pointers

    3. **Duplicates Case**: [1,2,2,3] and [2,3,3,4]
    - Check if current element equals last added element before adding
    - Works because arrays are sorted (duplicates must be adjacent)

    4. **Subset Case**: [1,2,3] and [2]
    - Handle mismatched array lengths with separate cleanup loops
    - Ensures we process all elements in both arrays

    ## Implementation Considerations
    - **Duplicate Checking**: Compare current element with last added result element
    - **Boundary Handling**: Process remaining elements when one array is exhausted
    - **Efficiency**: O(n+m) time complexity, O(n+m) space complexity

    ## Manual Tracing Example
    ```
    Example: arr1 = [1,2,3,4], arr2 = [2,3,4,4,5]

    i  j  arr1[i]  arr2[j]  Action                  result
    0  0     1        2     Add arr1[i], i++        [1]
    1  0     2        2     Equal, add once, i++,j++ [1,2]
    2  1     3        3     Equal, add once, i++,j++ [1,2,3]
    3  2     4        4     Equal, add once, i++,j++ [1,2,3,4]
    4  3    out       4     Skip duplicate, j++      [1,2,3,4]
    -  4    out       5     Add arr2[j], j++         [1,2,3,4,5]
    ```

    ## Key Takeaways
    1. Leverage the sorted property of input arrays
    2. Use adjacent element comparison for efficient duplicate detection
    3. Handle both common elements and unique elements properly
    4. Process remaining elements after one array is exhausted


"""



def helper_dupe_check(res:list,curr_arr_val:int):

    """
    Check if a value is a duplicate before adding it to the result list.
    
    In a sorted array union operation, duplicates will always be adjacent.
    This function checks if the current value is the same as the last element
    in the result list to prevent duplicates.
    
    Args:
        res: The result list containing merged unique elements so far
        curr_arr_val: The current value being considered for addition
    
    Returns:
        bool: True if the value is a duplicate, False otherwise
              False is returned if the result list is empty (always add first element)
    
    Example:
        If res = [1, 2, 3] and curr_arr_val = 3, returns True (duplicate)
        If res = [1, 2, 3] and curr_arr_val = 4, returns False (not duplicate)
        If res = [] and curr_arr_val = anything, returns False (empty list)
    """

    if len(res) == 0 or res[-1] != curr_arr_val:
            return False
    
    return True
            


def findUnion(arr1,arr2,n,m):


    """Find the union of two sorted arrays, removing duplicates.
    
    This function uses a merge approach similar to merge sort, taking
    advantage of the fact that both input arrays are already sorted.
    It handles duplicates both within each array and across arrays.
    
    Args:
        arr1: First sorted array
        arr2: Second sorted array
        n: Length of arr1
        m: Length of arr2
    
    Returns:
        list: A sorted array containing all unique elements from both arrays
    
    Time Complexity: O(n + m) - we traverse each array at most once
    Space Complexity: O(n + m) - in the worst case, all elements are unique
    
    Example:
        findUnion([1, 2, 3], [2, 3, 4]) returns [1, 2, 3, 4]
    """
   
    res = []
    i = 0 #index for arr1 
    j = 0 #index for arr2

    while i < n and j < m:

        #if curr el in arr1 < arr2
        if arr1[i] < arr2[j]:
            
            is_duplicate = helper_dupe_check(res,arr1[i])
            if not is_duplicate: 
                res.append(arr1[i])
                #only increment the pointer we took value from
                i+=1 

        elif arr1[i] > arr2[j]:

            is_duplicate = helper_dupe_check(res,arr2[j])
            if not is_duplicate: 
                res.append(arr2[j])
                #only increment the pointer we took value from
                j+=1 
        
        else: #arr1[i] == arr2[j]
            
            #since vals are the same, only dupe check for one necessary
            is_duplicate = helper_dupe_check(res,arr1[i])
            if not is_duplicate: 
                res.append(arr1[i])
                #increment both pointers here, need to move past the duplicate vals
                i+=1
                j+=1 
    
    while i < n:
        is_duplicate = helper_dupe_check(res,arr1[i])
        if not is_duplicate: 
            res.append(arr1[i])
            #only increment the pointer we took value from
            i+=1
                
    while j < m:
        is_duplicate = helper_dupe_check(res,arr2[j])
        if not is_duplicate: 
            res.append(arr2[j])
            #only increment the pointer we took value from
            j+=1 
    






#redo
def union_of_two_sorted_v2(arr1,arr2,n,m):

    

    """
    
        Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

        union is common and distinct elements, non repeating values. result should have elements in ascending order

        we're given 2 SORTED arrays arr1 and arr2

        input cases:
            basic, no overlap 
                handle: compare elements, add lesser value to res

                move ptr taken forward

            overlap case - > [1,2,3] [3,6,7]
                where arrays have common elements
                handle:    
                    add duplicate prevention check
                    so we arent adding the common element to res more than once.

                    we want to check that the curr element wasnt added last the res list

                    we can do this with simple check:
                        if curr != res[-1]

                    
            duplicates in indiv array case
                handle: same duplicate prevention applies here.

            subset case - one list is shorter than other
                handle: use seperate loops to add remaining elements of longer list
    
    """
    def helper_dupe_check(res:list,curr_arr_val:int):

   
        if len(res) == 0 or res[-1] != curr_arr_val:
                return False
        
        return True

        

    res = []
    i = 0
    j = 0

    while i < m and j < n:

        if arr1[i] < arr2[j]:
            is_duplicate = helper_dupe_check(res,arr1[i])
            if not is_duplicate:
                res.append(arr1[i])
            i+=1

        
        elif arr1[i] > arr2[j]:
            is_duplicate = helper_dupe_check(res,arr2[j])
            if not is_duplicate:
                res.append(arr2[j])
            j+=1

        else: #arr1[i] == arr2[j]
            is_duplicate = helper_dupe_check(res,arr2[j])
            if not is_duplicate:
                res.append(arr2[j])
            i+=1
            j+=1

    while i < m:
        is_duplicate = helper_dupe_check(res,arr1[i])
        if not is_duplicate:
            res.append(arr1[i])

        i+=1

    while j < n:
        is_duplicate = helper_dupe_check(res,arr2[j])
        if not is_duplicate:
            res.append(arr2[j])

        j+=1