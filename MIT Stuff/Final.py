'''
PROBLEM 1:

1-1: False
1-2: True
1-3: True
1-4: True
1-5: False
'''

'''
PROBLEM 2:

2-1: When a = A()
2-2: O(n)
2-3: False because a dictionary is mutable
2-4: Worst case foo_two is worse than foo_one
2-5: Polynomial
'''

'''
PROBLEM 3:


def sum_digits(s):
    digits = '1234567890'
    sums = []
    for i in s:
        if i in digits:
            sums.append(int(i))
    if len(sums) == 0:
        return ValueError
    else:
        return sum(sums)
'''

'''
PROBLEM 4:

import collections


def max_val(t):
    def flatten(t):
        if isinstance(t, collections.Iterable):
            return [a for i in t for a in flatten(i)]
        else:
            return [t]
    flat = flatten(t)
    return max(flat)
'''

'''
PROBLEM 5:

def cipher(map_from, map_to, code):
    key_code = {}
    decoded = ''
    for letter in range(len(map_from)):
        key_code[map_from[letter]] = map_to[letter]
    for i in code:
        decoded += key_code.get(i)
    return key_code, decoded
'''

'''
PROBLEM 6:

class Container(object):
    def __init__(self):
        self.vals = {}

    def insert(self, e):
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1

    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s


class Bag(Container):
    def remove(self, e):
        try:
            self.vals[e] -= 1
        except:
            self.vals[e] = 0

    def count(self, e):
        try:
            return self.vals[e]
        except:
            return 0

    def __add__(self, other):
        output = ''
        outputList = []

        for i in sorted(self.vals.keys()):
            if i in other.vals.keys():
                outputList.append([i, self.vals[i] + other.vals[i]])
            else:
                outputList.append([i, self.vals[i]])
        for j in sorted(other.vals.keys()):
            if j not in self.vals.keys():
                outputList.append([j, other.vals[j]])

        outputList = sorted(outputList)
        for k in outputList:
            output += str(k[0]) + ":" + str(k[1]) + "\n"
        return output


class ASet(Container):
    def remove(self, e):
        try:
            del self.vals[e]
        except:
            pass

    def is_in(self, e):
        if e in self.vals:
            return True
        else:
            return False
'''

'''
PROBLEM 7:

'''


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'


class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc

    def __str__(self):
        return str(self.center_loc)


class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """

    def __init__(self, center_loc, tent_loc=Location(0, 0)):
        """ Assumes center_loc and tent_loc are Location objects
        Initializes a new Campus centered at location center_loc
        with a tent at location tent_loc """
        # Your code here

    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        # Your code here

    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus.
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        # Your code here

    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain
        the string representation of the Location of a tent. The list should
        be sorted by the x coordinate of the location. """
        # Your code here