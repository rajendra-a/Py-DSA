"""The simplest solution to the sequence search problem is the sequential or 
linear search algorithm. this technique iterates over the sequence, one item at a time,
until specific item is found or all items have been examined.
In python target item can be found in a sequence using in operator."""
# The in operator is called membership operator


# but underneath, the in opearator implemented as linear search
""" Consider 1-D unsorted array of integer values 
To determine if value 31 is in array, the search begins with the value in the first element
if the first element does not contain the target value, the next element in sequential order is
compared to the target value. this process is repeated until the item is found.

what if the item not in the array?
suppose we want to search for value in the sample array"""
#the search begins at first item as before, but this time every item in the array is compared to 
#the target value. It can not be determined.
"""
here we can see the sequencial search algorithm which returns boolean value indicationg 
success or failure
this is same operation performed by the python in operator.
A count-controlled loop is used to traverse through the sequence during which each element is
compared against the target value"""

def linear_search(items, target):
    n = len(items)
    for i in range(n):
        # If the target is in the ith element, return True
        if items[i] == target:
            return True
    return False # if not found, return False

#searching sorted sequence
""" A linear search can also be performed on sorted sequence, which is a squence containing values
in a specific order, A linear search on sorted sequence works in same fashion as that for the
unsorted sequence, with one exception, it's possible to terminate the search early when the value is
not in the sequence instead of always having to perform a complete traversal"""

def sorted_linear_search(items, target):
    n = len(items)
    for i in range(n):
        # If the target is found in ith element, return True
        if items[i] == target:
            return True
        # If the target is larger than ith element, return False
        elif items[i] > target:
            return False
    return False # if not found, return False

# Finding smallest value
""" instead of searching for a specific value in an unsorted sequence,
suppose we wanted to search for the smallest value, which is equivalent to applying Pythons min()
function to the sequence. A linear search is performed as before, but this time we must keep track of
the smallest value found for each iteration through the loop"""

""" To prime the loop we assume """
#the first value in the sequence is the smallest
 """and start the comparisions at the second item.Since the smallest value can occur anywhere in
 the sequence, we must always perform a complete traversal, resulting in a worst case time O(n)"""

def findSmallest(theValues):
    n = len(theValues)
    # Assume the first item is the smallest value.
    smallest = theValues[0]
    # Determine if any other item in the sequence is smaller.
    for i in range(1, n):
        if theValues[i] < smallest:
            smallest = theValues[i]
    
    return smallest


