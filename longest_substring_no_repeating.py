"""
Given a string, find the length of the longest substring without repeating characters.
"""



"""
approach

use sliding window, keep expanding to right (adding to curr sequence) so long as we have no repeats
once we have a repeat, abandon curr seq, move to next iteration and begin from next consecutive character

abcabcbb

a
    a, length = 1 -> ab,length = 2 -> abc,length=3 -> abca X REPEAT, abandon
b
    b, length = 1 -> bc,length = 2 -> bca,length=3 -> bcab X REPEAT, abandon
c....
"""
def length_of_longest_sub(s):
    pass

print(length_of_longest_sub("abcabcbb"))