import random
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.label = 1 if x > y else -1
        self.colors = 'black' if self.label == 1 else 'pink'

def plot_dataset(n, width, height):
    points = [Point(random.uniform(0, width), random.uniform(0, height)) for _ in range(n)]

    x_vals = [p.x for p in points]
    y_vals = [p.y for p in points]
    colors = [p.colors for p in points]
    labels = [p.label for p in points]

    plt.figure(figsize = (8,6))
    plt.scatter(x_vals, y_vals, c = colors, alpha = 0.7)

    max_val = max(width, height)
    # x = y line
    plt.plot([0, max_val], [0, max_val], color = 'black', linestyle = '--')

    plt.xlim(0, width)
    plt.ylim(0, height)

    plt.show()
    return plt

# New dataset
plot_dataset(200, 100, 100)