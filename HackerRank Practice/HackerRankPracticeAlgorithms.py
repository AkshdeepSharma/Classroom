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

'''#!/bin/python3

import sys

#grades problem
n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())
    if grade >= 38:
        if grade % 5 == 4:
            print(grade + 1)
        elif grade % 5 == 3:
            print (grade + 2)
        else:
            print(grade)
    else:
        print(grade)'''

'''        
#!/bin/python3

import sys

#apples and oranges problem
s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

apples = 0
oranges = 0

for j in range(m):
    if (a + apple[j]) <= t and (a + apple[j]) >= s:
        apples = apples + 1
for i in range(n):
    if (b + orange[i]) <= t and (b + orange[i]) >= s:
        oranges = oranges + 1
print (apples)
print (oranges)'''
'''        
#!/bin/python3

import sys
#kangaroo problem
x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

kekm8 = False

if x1 > x2:
    for i in range((v1 * i) + x1 < ((v2 * i) + x2)):
        if ((v1 * i) + x1) != ((v2 * i) + x2):
            kekm8 = False
        else:
            kekm8 = True
            break
elif x1 < x2:
    for j in range((v1 * j)+ x1 > ((v2 * j) + x2)):
        if ((v1 * j) + x1) != ((v2 * j) + x2):
            kekm8 = False
        else:
            kekm8 = True
            break
elif x1 == x2:
    kekm8 = True

if kekm8 == True:
    print ('YES')
else:
    print ('NO')'''
'''    
#divisible sum pairs
#!/bin/python3

import sys

counter = 0

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

for i in range(n-1):
    for j in range(n-(i+1)):
        j = j + (i+1)
        if ((a[i]+a[j]) % k == 0):
            counter = counter + 1
print(counter)
'''
'''    
#bon apetite
#!/bin/python3

import sys

n,k = input().strip().split(' ')
c = [int(c_temp) for c_temp in input().strip().split(' ')]
b = int(input().strip())

if ((sum(c)- c[int(k)]) // 2) == b:
    print ('Bon Appetit')
else:
    print (b - ((sum(c) - c[int(k)]) // 2))

#4 1
#3 10 2 9
#7
'''
'''
#sock merchant
#!/bin/python3

import sys

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
counter = 0
pair = []
for i in range(n-1):
    if 

print(counter)
#9
#10 10 10  10 20 20 20 30 50'''
'''
#min max sums    
#!/bin/python

import sys


a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

def min_sum(a,b,c,d,e):
    return sum([a,b,c,d,e]) - max([a,b,c,d,e])

def max_sum(a,b,c,d,e):
    return sum([a,b,c,d,e]) - min([a,b,c,d,e])

print(min_sum(a,b,c,d,e), max_sum(a,b,c,d,e))
'''
'''
#Migratory birds
#!/bin/python3

import sys

n = int(input().strip())
types = list(map(int, input().strip().split(' ')))


def mode(types):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    for i in range(n):
        if types[i] == 1:
            count1 = count1+1
        elif types[i] == 2:
            count2 = count2+1
        elif types[i] == 3:
            count3 = count3+1
        elif types[i] == 4:
            count4 = count4+1
        else:
            count5 = count5+1

    countList = [count1,count2,count3,count4,count5]
    return countList.index(max(countList)) + 1

print(mode(types))
'''
'''
#between 2 sets
#!/bin/python3

import sys

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

counter = 0
count1 = 0

for i in range(len(b)-1):
    if (b[i + 1]) % b[i] == 0:
        count1 = count1 + 1
    if count1 == len(b) - 1:
        for j in range(len(a)):
            if b[0] % a[j] == 0:
                counter = b[0] // a[-1] - 1

print(counter)
#I FUCKING HATE THIS PROBLEM MAN
'''
'''
#Drawing book
#!/bin/python3

import sys

n = int(input().strip())
p = int(input().strip())

numberOfPagesTurned = 0

if p > (n/2):
    numberOfPagesTurned = (n - p) // 2
else:
    numberOfPagesTurned = (p // 2)

print(numberOfPagesTurned)
'''
'''
#cats and a MouseEvent
#!/bin/python3

import sys

q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]

    differenceXZ = abs(x-z)
    differenceYZ = abs(y-z)

    if differenceXZ < differenceYZ:
        print('Cat A')
    elif differenceXZ == differenceYZ:
        print('Mouse C')
    else:
        print('Cat B')
'''
'''
#The Hurdle Race
#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))

if k >= max(height):
    print('0')
elif k < max(height):
    print(max(height) - k)
'''

# climbing the ladder
# !/bin/python3

import sys

n = int(input().strip())
scores = [int(scores_temp) for scores_temp in input().strip().split(' ')]
m = int(input().strip())
alice = [int(alice_temp) for alice_temp in input().strip().split(' ')]

for i in range(len(alice)):
    for j in range(len(scores)):
        if alice[i] == scores[j]:
            if j == 0:
                print(str(j + 1) + ' equal')
            else:
                print(str(j) + ' equal')
        elif alice[i] > scores[j]:
            if j == 0:
                print(str(j + 1) + ' larger')
            else:
                print(str(j) + ' larger')

# 7
# 100 100 50 40 40 20 10
# 4
# 5 25 50 120
'''
for every 
'''
