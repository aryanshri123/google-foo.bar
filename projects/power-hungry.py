'''
PROBLEM DESCRIPTION:
You are given an array that represents the power output
of each panel on the commander's power grid. 
You must find the maximum output. Where the output is
the maximum of the product of a non-empty subset of the 
given array

EXAMPLE:
[2, 0, 2, 2, 0]
return 8

[-2, -3, 4, -5]
return 60

[-1, 3]
return -3
'''

def solution(xs):
    # create relevant lists
    negs = []
    pos = []
    zeros = []
    for n in xs:
        if n > 0:
            pos.append(n)
        elif n < 0:
            negs.append(n)
        else:
            zeros.append(n)
    # check if num negatives is odd
    all_negs = negs
    if len(negs) % 2 == 1:
        min_mag = max(negs)
        negs.remove(min_mag)
    # handle edge cases
    # positive solution possible
    if len(negs + pos) > 1:
        result = 1
        for n in negs + pos:
            result *= n
        return str(result)
    else:
        # if 0 is possible do it
        if len(zeros) > 0:
            return str(0)
        # negative must occur
        # ie one positive and one negative in xs
        else:
            result = 1
            for n in xs:
                result *= n
            return str(result)
        
        