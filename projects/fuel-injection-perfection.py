'''
PROBLEM DESCRIPTION:
There are three operations:
1) add one pellet
2) remove one pellet
3) divide entire group of fuel pellets by 2
    - only availabe if num pellets is even
Given a number, you want to find the minimum steps
it takes to reduce the number to 1 given the 3 operations

EXAMPLE:
4
return 2
4 -> 2 -> 1

EXAMPLE:
15
return 5
15 -> 16 -> 8 -> 4 -> 2 -> 1
'''

def solution(n):
    n = int(n)
    two_powers = [2 ** i for i in range(100)]
    count = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            if (n-1) in two_powers or (n-1) % 4 == 0:
                n -= 1
            elif (n+1) in two_powers or (n+1) % 4 == 0:
                n += 1
            else:
                n -= 1
        count += 1
    return count
