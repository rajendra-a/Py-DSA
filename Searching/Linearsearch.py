"""The simplest solution to the sequence search problem is the sequential or 
linear search algorithm. this technique iterates over the sequence, one item at a time,
until specific item is found or all items have been examined.
In python target item can be found in a sequence using in operator."""
# The in operator is called membership operator
if key in theArray:
    print("the key is in the array.")
else:
    print("the key is not in the array.")

# but underneath, the in opearator implemented as linear search
""" Consider 1-D unsorted array of integer values 
To determine if value 31 is in array, the search begins with the value in the first element
if the first element does not contain the target value, the next element in sequential order is
compared to the target value. this process is repeated until the item is found.

what if the item not in the array?
suppose we want to search for value 8 in the sample array
the search begins at first item as before, but this time every item in the array is compared to 
the target value. It can not be determined."""

# here we can see the sequencial search algorithm which returns boolean value indicationg 
# success or failure
# this is same operation performed by the python in operator

