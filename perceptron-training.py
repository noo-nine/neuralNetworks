import random
import matplotlib.pyplot as plt

learning_rate = 0.2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.label = 1 if x > y else -1
        self.colors = 'black' if self.label == 1 else 'pink'

#def plot_dataset(n, width, height):

# simple activation function
def sign(x):
    return 1 if x >= 0 else -1

class Perceptron:
    def __init__(self, n_weights, activation = sign):
        self.weights = [0] * n_weights
        self.activation = activation
        for i in range(n_weights):
            self.weights[i] = random.uniform(-1, 1)

    def guess(self, inputs):
        sum = 0
        for i in range(len(self.weights)):
            sum += inputs[i] * self.weights[i]
        output = self.activation(sum)
        return output
    
    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess
        # tuning the weights
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i] * learning_rate

n_points = 200
width, height = 100, 100
points = [Point(random.uniform(0, width), random.uniform(0, height)) for _ in range(n_points)]
perc = Perceptron(2)
epochs = [0]

fig, ax = plt.subplots(figsize = (8, 6))

def plot():
    ax.clear()
    x_s = []
    y_s = []
    color = []
    for p in points:
        inputs = [p.x, p.y]
        guess = perc.guess(inputs)
        x_s.append(p.x)
        y_s.append(p.y)
        color.append('green' if guess == p.label else 'red')

    ax.scatter(x_s, y_s, c=color, alpha=0.7)
    max_val = max(width, height)
    ax.plot([0, max_val], [0, max_val], color='black', linestyle='--')
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)

    fig.canvas.draw()
    
def on_click(event):
    epochs[0] += 1
    for p in points:
        perc.train([p.x, p.y], p.label)
    plot()

fig.canvas.mpl_connect('button_press_event', on_click)

plot()
plt.show()