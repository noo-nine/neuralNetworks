import random
import matplotlib.pyplot as plt
import time

learning_rate = 0.1

class Point:
    def __init__(self, x = None, y = None):
        self.x = x if x is not None else random.uniform(-1, 1)
        self.y = y if y is not None else random.uniform(-1, 1)
        self.label = 1 if self.x > self.y else -1   
    

def sign(x):
    return 1 if x >= 0 else -1

class Perceptron:
    def __init__(self, n_inputs, bias = 1, activation = sign):
        self.weights = [random.uniform(-1, 1) for _ in range(n_inputs)]
        self.bias = bias
        self.activation = activation

    def guess(self,inputs):
        sum = self.bias
        for i in range(len(inputs)):
            sum += self.weights[i] * inputs[i]
        return self.activation(sum)
    
    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i] * learning_rate
        self.bias += error * learning_rate

n_points = 200
p = Perceptron(2)
points = [Point() for _ in range(n_points)]

def plot(ax, epoch):
    ax.clear()
    # plot points
    for pt in points:
        inputs = [pt.x, pt.y]
        target = pt.label
        guess = p.guess(inputs)
        color = 'green' if guess == pt.label else 'red'
        ax.scatter(pt.x, pt.y, c = color)

    # plot perceptron decision boundary
    x_weights = [-1, 1]
    if p.weights[1] != 0:
        y_weights = [(-p.weights[0] * x - p.bias) / p.weights[1] for x in x_weights]
        ax.plot(x_weights, y_weights, color = 'blue', linestyle = '--', label = 'Perceptron boundary')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    plt.pause(0.01)

fig, ax  = plt.subplots(figsize = (6, 6))

epochs = 30
for epoch in range(epochs):
    for pt in points:
        p.train([pt.x, pt.y], pt.label)
    epoch += 1
    plot(ax, epoch)
    time.sleep(0.1)

plt.show()