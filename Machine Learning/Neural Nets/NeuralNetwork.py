import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt

class NeuralNetwork(object):

    def __init__(self):
        # Define Hyper-parameters
        self.input_layer_size = 2
        self.output_layer_size = 1
        self.hidden_layer_size = 3

        # Weights
        self.W1 = np.random.randn(self.input_layer_size, self.hidden_layer_size)
        self.W2 = np.random.randn(self.hidden_layer_size, self.input_layer_size)

    def forward(self, X):
        # Propagate inputs through network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3)
        return yHat

    def sigmoid(self, z):
        # Apply sigmoid activation function to scalar, vector, or matrix
        return 1 / (1 + np.exp(-z))

    def sigmoid_prime(self, z):
        # Gradient of sigmoid
        return np.exp(-z) / ((1 + np.exp(-z)) ** 2)

    def cost_function(self, X, y):
        # Compute cost for given X, y, use weights already stored in class
        self.yHat = self.forward(X)
        J = 0.5 * sum((y-self.yHat) ** 2)
        return J

    def cost_function_prime(self, X, y):
        # Computer derivative with respect to W and W2 for a given X and y
        self.yHat = self.forward(X)

        delta3 = np.multiply(-(y-self.yHat), self.sigmoid_prime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3)

        delta2 = np.dot(delta3, self.W2.T) * self.sigmoid_prime(self.z2)
        dJdW1 = np.dot(X.T, delta2)

        return dJdW1, dJdW2

    # Helper functions for interacting with other classes
    def get_params(self):
        # Get W1 and W2 unrolled into vector:
        params = np.concatenate((self.W1.ravel(), self.W2.ravel()))
        return params

    def set_params(self, params):
        # Get W1 and W2 using single parameter vector
        W1_start = 0
        W1_end = self.hidden_layer_size * self.input_layer_size
        self.W1 = np.reshape(params[W1_start:W1_end], (self.input_layer_size, self.hidden_layer_size))
        W2_end = W1_end + self.hidden_layer_size * self.output_layer_size
        self.W2 = np.reshape(params[W1_end:W2_end], (self.hidden_layer_size, self.output_layer_size))

    def compute_gradients(self, X, y):
        dJdW1, dJdW2 = self.cost_function_prime(X, y)
        return np.concatenate((dJdW1.ravel(), dJdW2.ravel()))


def compute_numerical_gradient(N, X, y):
    params_initial = N.get_params()
    numgrad = np.zeros(params_initial.shape)
    perturb = np.zeros(params_initial.shape)
    e = 1e-4

    for p in range(len(params_initial)):
        # Set perturbation vector
        perturb[p] = e
        N.set_params(params_initial + perturb)
        loss2 = N.cost_function(X, y)

        N.set_params(params_initial - perturb)
        loss1 = N.cost_function(X, y)

        # Compute numerical gradient
        numgrad[p] = (loss2 - loss1) / (2 * e)

        # Return value changed to zero
        perturb[p] = 0

    # Return params to original value
    N.set_params(params_initial)

    return numgrad


class Trainer(object):

    def __init__(self, N):
        # Make local reference to network
        self.N = N

    def callbackF(self, params):
        self.N.set_params(params)
        self.J.append(self.N.cost_function(self.X, self.y))

    def cost_function_wrapper(self, params, X, y):
        self.N.set_params(params)
        cost = self.N.cost_function(X, y)
        grad = self.N.compute_gradients(X, y)

        return cost, grad

    def train(self, X, y):
        # Make an internal variable for the callback function
        self.X = X
        self.y = y

        # Make an empty list to store costs
        self.J = []

        params0 = self.N.get_params()

        options = {'maxiter': 200, 'disp': True}
        _res = optimize.minimize(self.cost_function_wrapper, params0, jac=True, method='BFGS', args=(X, y), options=options, callback=self.callbackF)
        self.N.set_params(_res.x)
        self.optimizationResults = _res


# X = (hours sleeping, hours studying), y = Score on test
X = np.array(([3,5], [5,1], [10,2]), dtype=float)
y = np.array(([75], [82], [93]), dtype=float)

NN = NeuralNetwork()

T = Trainer(NN)

T.train(X, y)
plt.plot(T.J)
plt.grid(1)
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.show()
