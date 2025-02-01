def monotonic(lst, n):
    """Return True if lst is monotonic (either non-increasing or non-decreasing) for a given length n."""
    if n < 2:  # A list of length 1 or empty is trivially monotonic
        print("The list is monotonic.")
        return True
    
    increasing = decreasing = True  # Assume both are true initially
    
    for i in range(1, n):  # Iterate up to length n
        if lst[i] < lst[i - 1]:  # If we find a decrease
            increasing = False
        elif lst[i] > lst[i - 1]:  # If we find an increase
            decreasing = False
    
    if increasing or decreasing:
        print("The list is monotonic.")
        return True
    else:
        print("The list is not monotonic.")
        return False


# Test Case 1: 
lst1 = [1, 2, 2, 3]
n1 = len(lst1)
monotonic(lst1, n1)  # Should print "The list is monotonic."

# Test Case 2: 
lst2 = [3, 2, 1]
n2 = len(lst2)
monotonic(lst2, n2)  # Should print "The list is monotonic."

# Test Case 3: 
lst3 = [1, 3, 2]
n3 = len(lst3)
monotonic(lst3, n3)  # Should print "The list is not monotonic."

# Test Case 4: Non-decreasing list
lst1 = [1, 2, 2, 3]
n1 = len(lst1)
monotonic(lst1, n1)  # Should print "The list is monotonic."

# Test Case 5: 
lst2 = [5, 4, 4, 2]
n2 = len(lst2)
monotonic(lst2, n2)  # Should print "The list is monotonic."

# Test Case 6: 
lst3 = [1, 3, 2]
n3 = len(lst3)
monotonic(lst3, n3)  # Should print "The list is not monotonic."

# Test Case 7: 
lst4 = [10]
n4 = len(lst4)
monotonic(lst4, n4)  # Should print "The list is monotonic."

# Test Case 8: 
lst5 = [1, 3, 2, 4, 3]
n5 = len(lst5)
monotonic(lst5, n5)  # Should print "The list is not monotonic."


# Jan Dueppe