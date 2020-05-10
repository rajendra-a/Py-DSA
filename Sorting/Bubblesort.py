"""Sorting is the process of arranging or ordering a collection of items such that each item and its
its successor satisfy a prescribed relationship, The items can be simple values such as integers and reals
or more complex types, such as student records or dictionary entries. In etheir case, the order of items is
based on the value of sort key. The key is the value itself when sorting simple types or it can be
a specific component or combination of components when sorting complex types
sorting is one of the most studied program in computer science and extensive research done in this area
resulting in many different algorithms. while python provides sort() method for sorting list, it can not be
used with an array or other data structures. in addition, exploring the techiniques used by some of the sorting
algorithms  for improving the efficiency of the sort problem may provide ideas that can be used with other
types of problems
"""

# Bubble sort
"""A simple solution to the sorting problem is the bubble sort.
which rearranges the values by iterating over the list mulitple times, causing larger values 
to bubble to the top or end of the list.
"""

# the algorithm requires multiple passes over the cards, with each pass starting at the first card and
# ending one card earlier than on the previous iteration. during each pass, the cards in the first and 
# second positions are compared. if the first is larger than the second, the two cards are swapped

# sorts a sequence in ascending order
    def bubble_sort(thelist):
        n = len(thelist)
        # Perdform n-1 bubble operations on the sequence
        for i in range(n-1)
            #bubble the largest item to the end
            for j in range(i+n-1):
                if thelist[j] > thelist[j+1]: # swap the j and j+1 items
                    temp = thelist[j]
                    thelist[j] = thelist[j+1]
                    thelist[j+1] = temp