'''
QUESTION 1

balance = float(input())
annualInterestRate = float(input())
monthlyPaymentRate = float(input())

monthlyInterestRate = annualInterestRate / 12

for i in range(12):

    minMonthlyPayment = monthlyPaymentRate * balance
    unpaidBalance = balance - minMonthlyPayment
    balance = unpaidBalance + (monthlyInterestRate * unpaidBalance)

print('Remaining balance: ' + str(round(balance, 2)))
'''

'''
QUESTION 2

#3391
balance = 3926
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12
minPayment = 0
newBalance = 1
while newBalance > 0:
    newBalance = balance
    minPayment += 10
    for i in range(12):
        newBalance = (newBalance - minPayment) + (monthlyInterestRate * (newBalance - minPayment))

print('Lowest Payment: ' + str(minPayment))

'''

'''
QUESTION 3


balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12

lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12
minPayment = (lowerBound + upperBound) / 2
newBalance = 1
j = 0
while round(newBalance, 2) != 0:
    newBalance = balance
    minPayment = (lowerBound + upperBound) / 2

    for i in range(12):
        unpaidBalance = newBalance - minPayment
        newBalance = unpaidBalance + (monthlyInterestRate * unpaidBalance)

    if newBalance < 0:
        upperBound = minPayment
    elif newBalance > 0:
        lowerBound = minPayment

print("Lowest Payment = " + str(round(minPayment, 2)))
'''