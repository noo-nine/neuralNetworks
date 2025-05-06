import random

# simple activation function
def sign(x):
    if x >= 0:
        return 1
    if x < 0:
        return -1

class Perceptron:
    def __init__(self, n_weights, activation):
        self.weights = [0] * n_weights
        self.sign = activation
        for i in range(len(self.weights)):
            self.weights[i] = random.uniform(-1,1)
    
    def guess(self, inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum += inputs[i] * self.weights[i]
        output = self.sign(sum)
        return output
    
# creating a perceptron
p = Perceptron(2, sign)
print(p.guess([0.1, 0.5]))