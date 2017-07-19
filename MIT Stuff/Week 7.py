import pylab as plt
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
