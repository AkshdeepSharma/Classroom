import pylab as plt

'''
plt.show()
mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i ** 2)
    myCubic.append(i ** 3)
    myExponential.append(1.5 ** i)

plt.figure("Linear vs. Quadratic")
plt.clf()
plt.title('Linear vs. Quadratic')
plt.xlabel('Sample Points')
plt.ylabel('Functions')
plt.plot(mySamples, myLinear, label='Linear')
plt.plot(mySamples, myQuadratic, label='Quadratic')
plt.legend(loc='upper left')
plt.figure("Linear")
plt.clf()
plt.title('Linear')
plt.xlabel('Sample Points')
plt.ylabel('Linear Function')
plt.plot(mySamples, myLinear)
plt.figure("Quadratic")
plt.clf()
plt.title('Quadratic')
plt.xlabel('Sample Points')
plt.ylabel('Quadratic Function')
plt.plot(mySamples, myQuadratic)
plt.figure("Cubic")
plt.clf()
plt.title('Cubic')
plt.xlabel('Sample Points')
plt.ylabel('Cubic Function')
plt.plot(mySamples, myCubic)
plt.figure("Exponential")
plt.clf()
plt.title('Exponential')
plt.xlabel('Sample Points')
plt.ylabel('Exponential Function')
plt.plot(mySamples, myExponential)
'''


def retire(monthly, rate, terms):
    base = [0]
    savings = [0]
    mRate = rate / 12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + mRate) + monthly]
    return base, savings


def displayRetireMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label='Retire:'+str(monthly))
        plt.legend(loc='upper left')

displayRetireMonthlies([500, 600, 700, 800, 900, 1000, 1100], 0.05, 40 * 12)
