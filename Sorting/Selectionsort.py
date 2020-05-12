"""A Second sorting algorithm which improves the bubble sort and works in a fashion similar
to what a human may use to sort a list of values, is known as selection sort.
instead of swaping as we done with bubble sort, we are going to scan through items and select the 
smallest from among those on the list and leave the remaining and then we pick up the next small element
from the list and will be place it on the right side of the previously taken element. this process is continued
untill all items have been picked up and placed in our hand in the correct sorted order from smallest.
The Selection sort which improves on the bubble sort, makes mutiple passes over the sequence, but unlilke
the bubble sort, it only makes a single swap after each pass."""

# Sorts sequence in ascending order using the selection sort algorithm
def selection_sort(the_sequence):
    n = len(the_sequence)
    for i in range(n-1):
        # Assume the ith item is the smallest.
        small = the_sequence[i]
        # Determine if any other item contains a smaller value
        for j in range(i+1, n):
            if the_sequence[j]