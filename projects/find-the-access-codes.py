'''
PROBLEM DESCRIPTION:
Given a list of positive integers, find
how many "lucky triples" there are. A 
lucky triple is where x divides y and y
divdes z where position of x < y < z. 

EXAMPLE:
[1,1,1]
return 1
EXPLANATION:
1 divides 1 which divides 1

EXAMPLE:
[1,2,3,4,5,6]
return 3
EXPLANATION:
1 divides 2 which divides 4
1 divides 2 which divides 6
1 divides 3 which divides 6
'''

def solution(l):
    c = [0] * len(l)
    count = 0
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                c[i] += 1
                count += c[j]
    return count
    
                        
