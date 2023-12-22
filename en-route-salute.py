'''
PROBLEM DESCRIPTION:
Soldiers must salute each other when they see each other.
They salute one at a time. Given a hallway configuration,
you must figure out how many total salutes are given.
- represents an empty space
> represents a solider walking right
< represents a soldier walking left

EXAMPLE:
">----<"
return 2

EXAMPLE:
"<<>><"
return 4
'''

def solution(s):
    result = 0
    for i, c in enumerate(s):
        if c == '>':
            result += s.count('<', i, len(s))
        elif c == '<':
            result += s.count('>', 0, i)
    return result