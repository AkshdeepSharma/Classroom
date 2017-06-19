import time
from random import randrange
"""
'''
[5,4,2,1,0]]
finding the smallest number in a list. Compare 5 to 4, 2, 1 , 0, then 4 etc. This is O(n^2), therefore shit.
'''

def find_min_quadratic(alist):
    overall_min = alist[0]
    for i in alist:
        isSmallest = True
        for j in alist:
            if i > j:
                isSmallest = False
        if isSmallest:
            overall_min = i
    return overall_min

#print(find_min ([5, 4, 2, 1, 0]))
''' since there are 2 loops, and each loop is iterating over n once, then it is O(n^2). This is not good.'''

for listSize in range(1000,10001,1000):
    alist = [randrange(100000) for x in range (listSize)]
    start = time.time()
    print(find_min_quadratic(alist))
    end = time.time()
    print ('size: %d. Time: %f', listSize, end-start)
''' holy shit! it's 6.1 seconds to run this for a 10000 length list.'''
"""    
from msilib import Binary
'''
def find_min_linear(alist):
    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i
    return minsofar

for listSize in range(1000,10001,1000):
    alist = [randrange(100000) for x in range (listSize)]
    start = time.time()
    print(find_min_linear(alist))
    #print(find_min_quadratic(alist))
    end = time.time()
    print ('size: %d. Time: %f', listSize, end-start)
'''    
'''lists are different from dictionaries. Dicts allow you to access elements based on a key rather than a position'''
'''stacks are fundamentally important because they canbe used to reverse the order of items. LIFO. Like a Back
   button on a browswer.'''
''' Stack code to reverse an input.
from test import testEqual
from pythonds.basic.stack import Stack

def revstring(mystr):
    m = Stack()
    revString = ''
    for character in mystr:
        m.push(character)
    while not m.isEmpty():
        revString = revString + m.pop()
    return revString

testEqual(revstring('apple'),'elppa')
testEqual(revstring('x'),'x')
testEqual(revstring('1234567890'),'0987654321')
'''
'''On 3.9, might wanna review 3.6-3.8, and make sure you go over 1.8-1.17'''
'''1.12: generate a program that will check if a string is similar to another one based on score.
import random

def generate_a_string (stringLength):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    reserveString = ""
    for i in range(stringLength):
        reserveString = reserveString + alphabet[random.randrange(27)]
    return reserveString
        
def score_of_string (goal, testString):
    numSame = 0
    for i in range(len(goal)):
        if goal[i] == testString[i]:
            numSame = numSame + 1
    return numSame / len(goal)

def main ():
    goalString = 'methinks it is like a weasle'
    while score_of_string(goalString, generate_a_string(28) < 1):
        print(score_of_string, generate_a_string)
        break
'''
'''1.13 object oriented programming. This is an example of the fraction class.
   Shallow equality is when 2 objects are only equal if they are referencing the same object. If 2 different
   objects have the same numerator and denominator, they will not be equal. If they were equal, it's called deep
   equality. T
   
   
def lcd (m, n):
    while m%n != 0:
        oldm = m
        oldn = n
            
        m = oldn
        m = oldm%oldn
        
class Fraction:
    
    def __init__(self, top, bottom):
        
        self.num = top
        self.den = bottom
    
    def __str__(self):
        return str(self.num) + '/' + str(self.den)
    
    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den + otherfraction.num
        newden = self.den * otherfraction.den
        common = lcd(newnum, newden)
        
        return Fraction(newnum//common, newden//common)
    
    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - self.den + otherfraction.num
        newden = self.den * otherfraction.den
        common = lcd(newnum, newden)
        
        return Fraction(newnum//common, newden//common)
    
    def __mul__(self, otherfraction):
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = lcd(newnum, newden)
        
        return Fraction(newnum//common, newden//common)

    def __truediv__(self, otherfraction):
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        common = lcd(newnum, newden)
        
        return Fraction(newnum//common, newden//common)    

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        
        return firstnum < secondnum
    
    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        
        return firstnum > secondnum
        
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        
        return firstnum == secondnum

myf = Fraction(3,5)
print(myf)
'''

''' 1.13 object oriented programming. Using a logic gate parent function to make a logic gate program
    IS A relationship talks about the relationship between parent-child. HAS A relationship refers to
    a relationship that doesn't have inheritance, but are related. The LogicGate/BinaryGate are a IS A
    relationship, the connector and LogicGate are a HAS A relationship.

class LogicGate:
    
    def __init__(self, n):
        self.label = n
        self.output = None
        
    def get_label(self):
        return self.label
    
    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output
    
class BinaryGate(LogicGate):
    
    def __init__(self, n):
        LogicGate.__init__(self, n)
        
        self.pinA = None
        self.pinB = None
        
    def get_pinA (self):
        return int(input("Enter Pin A input for gate " + self.get_label() + "-->"))
    
    def get_pinB (self):
        return int(input("Enter Pin B input for gate " + self.get_label() + "-->"))
    
class UnaryGate(LogicGate):
    
    def __init__(self, n):
        LogicGate.__init__(self, n)
        
        self.pin = None
        
    def get_pin(self):
        return int(input("Enter Pin input for gate " + self.get_label() + "-->"))
    
class AndGate(BinaryGate):
    
    def __init__(self, n):
        BinaryGate.__init__(self, n)
    
    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    
    def __init__(self, n):
        BinaryGate.__init__(self, n)
        
    def perform_gate_logic(self):
        a = self.get_pinA()
        b = self.get_pinB()
        
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    
    def __init__(self, n):
        UnaryGate.__init__(self, n)
        
    def perform_gate_logic(self):
        pin = self.get_pin()
        
        if pin == 1:
            return 0
        elif pin == 0:
            return 1

class NandGate(AndGate):
    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1

class NorGate(OrGate):
    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1
    
class Connector:
    
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        
        tgate.setNextPin(self)
        
    def get_from(self):
        return self.fromgate
    
    def get_to(self):
        return self.togate
    
def set_next_pin(self, source):
    if self.pinA == None:
        self.pinA = source
    else:
        if self.pinB == None:
            self.pinB = source
        else:
            raise RuntimeError("Error: No Empty Pins Available")
                
def get_pinA(self):
    if self.pinA == None:
        return input("Enter Pin A input for gate " + self.getName() + "-->")
    else:
        return self.pinA.get_from().get_output()
        
def main():        
    g1 = AndGate("G1")
    print (g1.get_output())
    g2 = OrGate("G2")
    print (g2.get_output())
    g3 = NotGate("G3")
    print (g3.get_output())
    
main()
'''
'''
   3.9: infix, prefix and postfix expressions.
   Prefix and postfix are easier for computers to understand = faster runtimes. Infix easier for humans.
   Simply move the operator to before/after the operands.
   For example: A * B + C * D
   A B * C D * + = postfix
   * + A B * C D = prefix
   
#algorithm to convert infix to postfix. I didn't really look over it, this is kinda boring.   
from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
   

'''
'''
   QUEUES: First in first out.
'''
class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self,item):
        self.items.insert(0,item)
                
    def dequeue(self):
        return self.item.pop()
    
    def size(self):
        return len(self.items)
    