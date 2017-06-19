#!/bin/python3

'''import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

def diagonal_difference(a):
    primary = sum(a[i][i] for i in range(n))
    secondary = sum(a[i][n-i-1] for i in range(n))
    return abs(primary-secondary)
 
print (diagonal_difference(a))'''

'''import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

def array_fractions(arr):
    positive1 = 0
    negative1 = 0
    zeroe1 = 0
    for i in range(n):
        if arr[i] > 0:
            positive1 = positive1 + 1
        elif arr[i] < 0:
            negative1 = negative1 + 1
        else:
            zeroe1 = zeroe1 + 1   
    print (round(positive1/n,6))
    print (round(negative1/n,6))
    print (round(zeroe1/n,6))
    return ''

print (array_fractions(arr))'''
'''
#!/bin/python3

import sys

n = int(input().strip())
    
def create_staircase(n):
    for i in range(n):
        print (' ' * (n-(i+1)) + '#' * (i+1))
    return ''

print(create_staircase(n))'''

'''#!/bin/python3

import sys

time = input().strip()

a,b,c = time.split(':')

if time[-2:] == 'PM' and int(a)<12:
    a = int(a) + 12
elif time[-2:] == 'AM' and int(a) == 12:
    a = '00'
    
print (str(a)+':'+str(b)+':'+str(c[:-2]))'''






