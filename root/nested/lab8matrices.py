#----------------------------(EXERCISE 1)--------------------------#

#(TO DO 1.1)
#1. Define a function with name 'newMatrixTranspose'.
#2. The function accepts one input parameter, the matrix to be transposed.
#3. Print the input matrix and its size (i.e. number of rows and number of columns).
#   Note: Look at the sample output and use the same statement in your code.
#4. Find the transpose of the given matrix using the following steps:
#4.1. Calculate the size (rows and columns) of the transposed matrix
#4.2. Initialize the transposed matrix with all zeros.
#4.3. Now, use 'nested for' to set the actual elements of the transposed matrix.
#5. Print the size of the transposed matrix. Note: Look at the sample output and use the same statement in your code.
#6. Print the transposed matrix.
#Note: Use 'print()' at suitable postions in the code to print on a new line.

#Write your code here


def newMatrixTranspose(matrix):
    print 'We have to find the transpose of the matrix shown below.'
    mat_rows = len(matrix)
    mat_cols = len(matrix[0])
    print 'It is of size =', mat_rows, '*', mat_cols
    for row in matrix:
        for col in row:
            print col, '\t',
        print
    print 'The transpose of the given matrix is as shown below.'
    print 'The transpose has a size =', len(matrix[0]), '*', len(matrix)
    transpose = [[0]*mat_rows]*mat_cols

    for i in range(0, mat_cols):
        for j in range(0, mat_rows):
            transpose[i][j] = matrix[j][i]

    for row in transpose:
        for col in row:
            print col, '\t',
        print


#(TO DO 1.2)
#1. Define a function with name 'inplaceTranspose'.
#2. The function accepts one input parameter, the square matrix to be transposed.
#3. Print the input Square matrix and its size.
#   Note: Look at the sample output and use the same statement in your code.
#4. Using 'nested for' and 'if condition' calculate the in-place transpose of the given square matrix.
#5. Print the size of the transposed matrix
#6. Print the transposed matrix.
#Note: Use 'print()' at suitable points in the code to print on a new line.

#Write your code here


def inplaceTranspose(matrix):
    print 'We have to find the transpose of the square matrix shown below.'
    size = len(matrix)
    print 'It is of size =', size, '*', size

    for i in range(size):
        for j in range(size):
            print matrix[i][j], '\t',
        print

    for i in range(size):
        for j in range(size):
            if i <= j:
                continue
            tmp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = tmp

    for i in range(size):
        for j in range(size):
            print matrix[i][j], '\t',
        print


#----------------------------(EXERCISE 2)--------------------------#
#The main()function
#(TO DO 2.1)
#1. Call the function newMatrixTranspose to transpose matrixA
#2  Call the function newMatrixTranspose to transpose matrixB
#3  Check if EACH of the given matrix is square or rectangular. If it is square then call a function named 'inplaceTranspose'.


def main():
    matrixA = [[1, 8, 9], [6, 2, 3], [4, 5, 7]]  # do not make any changes to this line
    matrixB = [[11, 22, 33], [44, 55, 66]]   # do not make any changes to this line
#Write your code here
    #newMatrixTranspose(matrixA)
    #newMatrixTranspose(matrixB)
    inplaceTranspose(matrixA)

if __name__ == '__main__':
    main()