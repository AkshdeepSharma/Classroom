#!/usr/bin/env python3

max_value = int(input())
array = []

def Sieverino (array):
    l = 1
    # creates an array from 2 to max_value
    for i in range(2, max_value + 1):
        array.append(i)

    for i in range(len(array)):
        l = l + 1
        m = 2
        for j in range(len(array)):
            product = l * m
            if product > max_value:
                break
            elif product in array:
                array.remove(product)
            m = m + 1
    return (array)
    

print (Sieverino(array))