# Function that takes a list [a,b] of length 2 and returns [a, min(a,b)+1, b]
import copy
import matplotlib.pyplot as plt

def expand_list(l):
    return [l[0], min(l[0],l[1])+1]

# def manipulate_str(s):
#     for i in range(len(s)):
#     db = s[i,i+2]

def expand_consecutive_pairs(lst):
    """
    Applies expand_list to each consecutive pair in the input list.
    Each pair's expanded list fully replaces the pair in the output.
    """
    if len(lst) < 2:
        return lst.copy()  # nothing to do

    new_pairs = []
    for i in range(len(lst) - 1):
        a, b = lst[i], lst[i+1]
        new_pairs.append(expand_list([a,b]))

    out = flatten(new_pairs)
    out.append(lst[-1])
    return out

def flatten(xss):
    return [x for xs in xss for x in xs]

def multiple_expand(input, n):
    new = input
    for i in range(n):
        # print(new)
        new = copy.copy(expand_consecutive_pairs(new))
    return new


