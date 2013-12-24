#-------------------------------------------------------------------------------
# Name: George Mason.
# Project X
# Section XXX
# Due Date: MM/DD/YYYY
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: (list any lecture slides, text book pages, any other resources)
# Note: you may not use code from websites, so don't bother looking any up.
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
#       10        20        30        40        50        60        70        80
#-------------------------------------------------------------------------------	


# Check whether x is even or not.
# Return boolean True if x is even, otherwise return False  
def is_even(x):
    return (x % 2) == 0


# Remove all even numbers from the list xs
# Updates the list xs by removing all even numbers
def remove_evens(xs):
    xs[:] = [x for x in xs if not is_even(x)]
    return xs

# Find and return a copy of the minimum value in a given
# array xs
def minval(xs):
    theMin = xs[0]
    for x in xs:
        if theMin > x:
            theMin = x
    return theMin

# Find and return the index of the minimum value
# in a list of numbers
def min_index(xs):
    theMin = minval(xs)
    minIndex = -1
    for i in range(len(xs)):
        if xs[i] == theMin:
            minIndex = i
            break
    return minIndex

# Find and removes a given value val from a list
# of nmbers xs.
# Returns True if val is found, otherwise returns False	
def remove_value_once(val, xs):
    index = -1
    for i in range(len(xs)):
        if xs[i] == val:
            index = i
            break
    if index >= 0:
        xs.remove(xs[index])
        return True
    else:
        return False

# Given a list of numbers, you will return a copy of the list with all elements in sorted
# (ascending) order. The given list should be unchanged.
def min_sorted(xs):
    result = []
    copy = xs[0:]

    while len(copy) > 0:
        theMin = minval(copy)
        remove_value_once(theMin, copy)
        result.append(theMin)

    return result

# Given a list of numbers, you will return the list with all elements in sorted
# (ascending) order. The given list is also modified.
def min_sort(xs):
    xs[:] = min_sorted(xs)
    return xs

# Find and return the median value of the list xs when its sorted
def median(xs):
    sorted_xs = min_sorted(xs)
    size = len(xs)
    median = sorted_xs[int((size - 1) / 2)]
    return median

# Find and return the k-th min of a given list xs
def kth(k, xs):
    sorted_xs = min_sorted(xs)
    return sorted_xs[k]

# Given two lists of values, create and return a list of tuples that "zip" up 
#the values from the two lists together
def zip(xs, ys):
    minLen = minval([len(xs), len(ys)])
    pair_list = []
    for i in range(minLen):
        pair_list.append((xs[i], ys[i]))
    return pair_list

#Given two lists of numbers, create a new list of numbers by multiplying the
# same-indexed values.
def pairwise_multiply(xs, ys):
    minLen = minval([len(xs), len(ys)])
    result = []
    for i in range(minLen):
        result.append(xs[i] * ys[i])
    return result

# Given two lists of numbers, return a single number found by multiplying each
# same-indexed pair of numbers, and adding the results together.
def dot_product(xs, ys):
    minLen = minval([len(xs), len(ys)])
    product = 0
    for i in range(minLen):
        product = product + xs[i] * ys[i]
    return product

# Return a list with n copies of val.	
def repeat(val, n):
    result = val * n
    return result

# Given two lists of values, create (and return) the interleaved 
# version by making a new list with the first value of xs, then the first 
# value of ys, then the second value of xs, second value of ys,and so on.
def interleave(xs, ys):
    result = []
    minLen = minval([len(xs), len(ys)])
    i = 0
    while i < minLen:
        result.append(xs[i])
        result.append(ys[i])
        i += 1
    result = result + xs[i:] + ys[i:]
    return result

# Shuffle a given list xs n times
def shuffle(xs, n=1):
    if n <= 0:
        return None

    mid = int(len(xs) / 2)
    ys = xs[:mid]
    zs = xs[mid:]

    result = interleave(ys, zs)
    xs[:] = result
    shuffle(xs, n - 1)

# Create and return a list of all possible pairs from values 
# in xs and values in ys
def all_pairs(xs, ys):
    result = []
    for x in xs:
        for y in ys:
            result.append((x, y))

    return result

# Given a list of pairs, construct and return a new list by 
# calling str() on each of the two values in a pair, concatenating 
# those results together, and adding into your new list at the same
# index as the original pair from the original list
def stringify_pairs(pairs):
    result = []
    for (x, y) in pairs:
        s = str(x) + str(y)
        result.append(s)

    return result

# create a new fresh deck of cards
def new_deck():
    pips = "23456789TJQKA"
    suits = "CDHS"
    pairs = all_pairs(list(pips), list(suits))
    result = stringify_pairs(pairs)
    return result

# Given a list of more than one dimension, create and return a new list by collapsing that
# outermost dimension
def flatten(xs):
    result = []
    for x in xs:
        if isinstance(x, list):
            for y in x:
                result.append(y)
        else:
            result.append(x)
    return result

# Shuffle multiple decks with given n times passed as variable number of arguments 
def multishuffle(*args, n=1):
    results = []
    i = 0
    while True:
        is_appended = False
        for arg in args:
            if i < len(arg):
                results.append(arg[i])
                is_appended = True
        i += 1
        if not is_appended:
            break
    if n > 1:
        shuffle(results, n)
    return results

# Given	a python function and a sequence of values, create a new list
# by calling the function on each value in the sequence and placing the
# the results in a returned list
def map(f, xs):
    result = []
    for x in xs:
        result.append(f(x))
    return result

# Combine elements of xs and ys together while using the operator
# f, generating a new list
def zip_with(f, xs, ys):
    minLen = minval([len(xs), len(ys)])
    result = []
    for i in range(minLen):
        result.append(f(xs[i], ys[i]))

    return result

# Inspect each item of xs; if calling f on it returns the True value
#, include it in your results.
def filter(f, xs):
    result = []
    for x in xs:
        if f(x):
            result.append(x)
    return result

# Given a function f, a starting value z, and a list xs, keep on
# combining z and the next value from xs with f. Return the result
def fold(f, z, xs):
    result = z
    for x in xs:
        result = f(result, x)

    return result

# place this at the end of your file:
def main():
    import tester
    tester.runtests(__file__)

if __name__ == "__main__":
    main()