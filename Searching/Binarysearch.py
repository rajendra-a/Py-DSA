""" The linear search algorithm for a sorted sequence produced a slight improvement over the 
linear search with an unsorted sequence, but both have linear time complexity in the worst case.
To improve the search time for a sorted sequence we can modify the search technique itself.

Consider an example where you are given a stack of exams, which are in alphabetical order. and are
asked to find exam of jessica. in performing this task, most people would not begin with the first 
exam and flip through one at a time until the requested exam is found, as would be done with a linear
search. instead, you would probably flip to the middle and determine if the requested exam comes alphabetically
before or after that one. Assuming Jessicas paper follows alphabetically after the middle one,
you know it can't be possibly be in the top half of the stack. instead you would probably continue
searching in similar way by splitting the remaining stack of exams in half to determine which portion
contains Jessica's exam. this an example of devide and conquer strategy, which entails dividing large
into 
"""

#Algo description
"""The binary search algorithm Works in similar fashion to the process described above and can be 
applied to a sorted sequence. The starts by examining the middle item of the sorted sequence, resuliting in
one of the three possible conditions:
1. The middle item is the target value
2. The target value less than the middle item
3. The target values larger than the middle value
Since the sequence is ordered, we can eliminate half the values in the list when the target value is not found
at the middle position 
The process is repeated on the remaining items
The process would continue until either the target value was found or we had eliminated all values from
consideration"""

# The variables high and low are used to mark the range of elements in the sequence currently under
# consideration.
# when the search begins, this range is the entire sequence since the target item can be anywhere with in
# the sequence
# The first step in each iteration is to determine the mid point of the sequence.
# if the sequece contains even number of elements, the midpoint will be chosen such that the left sequence
# contain one less item than the right

def binarySearch(theValues, target):
    # Starts with the entire sequence of elements
    low = 0
    high = len(theValues)-1
    
    # Repeatedly subdivide the sequence in half until the target is found
    while low <= high:
        # Find the midpoint of the sequence
        mid = (low+high)//2
        # Does the midpoint contain target ?
        if theValues[mid] == target:
            return True
        # Or does the target preced the midpoint?
        elif target < theValues[mid]
            high = mid - 1
        # or does it follow the midpoint?
        else:
            low = mid + 1
        
        # If the sequence cannot be subdivided further, we are done
    return False
""" After computing the midpoint, the corresponding element in that position is examined.
If the midppoint contains the target, we immediately return True. Otherwise, we determine if the 
target is less than the item at the midpoint or greater. if it is less, we adjust the high marker to 
be one less than the midpoint and if it is greater, we adjust the low marker to be one greater than the 
midpoint. In the next iteration of the loop, the only portion of the sequence considered are those elements
between the low and high markers, as adjusted. This process is repeated until the item is found or the low
marker becomes greater than the high marker. this condition occurs when there are no items left to be
processed, indicating the target is not in the sorted sequence."""