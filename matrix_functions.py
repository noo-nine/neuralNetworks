import random

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []

        for i in range( 0, self.rows):
            row = []
            for j in range(0, self.cols):
                row.append(0)
            self.matrix.append(row)


    def randomize(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = random.randint(1,10)


    def add(self, n):

        # element-wise function
        if isinstance(n, Matrix):
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] += n.matrix[i][j]
        
        # scalar funxtion
        else:
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    self.matrix[i][j] += n
    

    # matrix multiplication

    @staticmethod
    def mat_mul(m1, m2):
        if m1.cols != m2.rows:
            print('No of cols in m1 should be equal to no of rows in m2')
            return None
            
        result = Matrix(m1.rows, m2.cols)
        for i in range(m1.rows):
            for j in range(m2.cols):
                sum = 0
                for k in range(m1.cols):
                    sum += m1.matrix[i][k] * m2.matrix[k][j]
                result.matrix[i][j] = sum
        return result
    
    # scalar function
    def mul_scalar(self, n):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                self.matrix[i][j] *= n

    # mapping function
    def map(self, func):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                val = self.matrix[i][j]
                self.matrix[i][j] = func(val)
    
    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[j][i] = self.matrix[i][j]
        return result
    
    @staticmethod
    def fromArray(arr):
        r = Matrix(len(arr), 1)
        for i in range(0, len(arr)):
            r.matrix[i][0] = arr[i]
        return r 
    
    def toArray(self):
        arr = []
        for i in range(self.rows):
            for j in range(self.cols):
                arr.push(self.matrix[i][j])
        return arr

    def __str__(self):
        return '\n'.join(" ".join(f'{val}' for val in row) for row in self.matrix)


# m = Matrix(4,5)
# m.randomize()
# print('Matrix 1\n', m, '\n Matrix 2')
# n = Matrix(5, 2)
# n.randomize()
# print(n, '\n Product')
# product = Matrix.mat_mul(m, n)
# print(product)

# print('array')
# array = [1,2,3]
# a = Matrix.fromArray(array)
# print(a)