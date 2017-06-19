from math import *

def polysum (n, s):
    '''
    input: 
    n =  number of sides of the polygon 
    s = length of each side
    output:
    returns area of polygon + perimeter of polygon squared
    '''
    area = (0.25 * n * s**2) / (tan (pi / n))
    perimeter = n * s
    sum = round(area + perimeter ** 2, 4)
    return sum

print(polysum(3.213,3))