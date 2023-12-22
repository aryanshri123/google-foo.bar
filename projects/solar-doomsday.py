'''
PROBLEM DESCRIPTION:
There is a sheet with a given area.
You want to make a bunch of little squares out of that sheet.
Do this by taking the biggest square that will fit in area
and keep going

EXAMPLE:
area = 12
Then you can make a 3x3 square (area of 9). So you have 3 
area units left. Out of that, you can make 3 1x1 squares.
return [9, 1, 1, 1]

EXAMPLE:
area = 24
Then you can make a 4x4 square (area of 16). So you have 8
area units left. Out of that, you can make a 2x2 square
(area of 4). Then you have 4 area units left, so you can make
another 2x2 square.
return [16, 2, 2]
'''

def solution(area):
    result = []
    while area != 0:
        biggest = (int(area**(0.5)))**2
        area -= biggest
        result.append(biggest)
    return result