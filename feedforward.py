import math

def sigmoid(x):
    return 1/(1 + math.exp(-x))

from matrix_functions import Matrix

class neuralnetwork:

    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes
        # weights between input and hidden nodes
        self.weights_ih = Matrix(self.hidden_nodes, self.input_nodes) 
        # weights between hidden and output nodes
        self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)

        self.weights_ih.randomize()
        self.weights_ho.randomize()

        self.bias_h = Matrix(self.hidden_nodes, 1)
        self.bias_o = Matrix(self.output_nodes, 1)

        self.bias_h.randomize()
        self.bias_o.randomize()

    def feedforward(self, input_arr):
        # input received to the hidden nodes
        inputs = Matrix.fromArray(input_arr)
        hidden = Matrix.mat_mul(self.weights_ih, inputs)
        hidden.add(self.bias_h)
        hidden.map(sigmoid)
        # hidden node outputs

        #output layer inputs
        output = Matrix.mat_mul(self.weights_ho, hidden)
        output.add(self.bias_h)
        output.map(sigmoid)

        return output


#a = 2
#req = sigmoid(a)
#print(req)