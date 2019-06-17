import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):

            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
              
        if self.h == 1:
            det = self.g[0][0]
        else:
        
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
        
            det = a*d - b*c
            
        return det

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace = 0
        
        for i in range(self.w):
            trace += self.g[i][i]
            
        return trace
    
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here

        if self.h == 1:
            inverse = zeroes(1,1)
            inverse[0][0] = 1/self.g[0][0]
            return inverse
            
        else:
            inverse = []
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
      

            newInverse = [[d, -b],[-c, a]]

            for i in range(self.h):
                newRow = []
                for j in range(self.w):
                    num = newInverse[i][j]/(self.determinant())
                    newRow.append(num)

                inverse.append(newRow)

            return Matrix(inverse)
        

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
       
        matrix_transpose = []

        numCols = self.w
        numRows = self.h

        for j in range(numCols):
            newCol=[]
            for i in range(numRows):
                newCol.append(self.g[i][j])
            matrix_transpose.append(newCol)

        return Matrix(matrix_transpose)
        

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #

        matrixSum = []

        numRows = self.h
        numCols = self.w

        for i in range(numRows):
            newRow = []
            for j in range(numCols):
                newRow.append(self.g[i][j]+other.g[i][j])
            matrixSum.append(newRow)

        return Matrix(matrixSum)

        
        
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        
        matrixNeg=[]
        
        numRows = self.h
        numCols = self.w

        for i in range(numRows):
            newRow = []
            for j in range(numCols):
                newRow.append(-self.g[i][j])
            matrixNeg.append(newRow)
        
        return Matrix(matrixNeg)

    
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        
        matrixSubtract = []

        numRows = self.h
        numCols = self.w

        for i in range(numRows):
            newRow = []
            for j in range(numCols):
                newRow.append(self.g[i][j]-other.g[i][j])
            matrixSubtract.append(newRow)

        return Matrix(matrixSubtract)
                
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        product = []     
        matrixBT = other.T()
           
        numRowSelf = self.h
        numRowOther = other.h
        numColOther = other.w
        
        for i in range(numRowSelf):
            newProduct = []
            for j in range(numColOther):
                total = 0
                for l in range(numRowOther):
                    total += self.g[i][l]*matrixBT[j][l]
                newProduct.append(total)
            product.append(newProduct)

        return Matrix(product)    
    
    
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        numRows = self.h
        numCols = self.w
               
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #

            result = zeroes(numRows,numCols)

            for i in range(numRows):
                for j in range(numCols):
                    result[i][j] = self.g[i][j]*other

            return result