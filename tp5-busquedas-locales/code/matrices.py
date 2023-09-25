# Module to create and show matrices easily and also some encoding
from math import ceil

def create_matrix(rows, columns): 
    # Creates an empty matrix with the rows and columns specified and returns it

    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            matrix[i].append(None)

    return matrix

def print_matrix(matrix):
    # Prints the matrix on screen

    rows = len(matrix)
    for i in range(rows):
        columns = len(matrix[i])
        for j in range(columns):
            print(matrix[i][j], end=' ')
        print()

def print_matrix_without_spaces(matrix):
    # Prints the matrix on screen without blank spaces between the numbers

    rows = len(matrix)
    for i in range(rows):
        columns = len(matrix[i])
        for j in range(columns):
            print(matrix[i][j], end='')
        print()

def fill_matrix(matrix, filler):
    # Fills the whole matrix with the filler, for example if the filler is the number 0 the matrix will be filled with all numbers 0

    rows = len(matrix)
    for i in range(rows):
        columns = len(matrix[i])
        for j in range(columns):
            matrix[i][j]= filler
            
def position_by_counting(posY: int, posX : int, matrixSizeX : int) -> int:
    # Returns an encoding of a position of a matrix, to understand this encoding 1=(y=0,x=0), 2=(y=0, x=1) and so on, basically instead of x and y the position is given by counting from 1 to matrixSizeX*matrixSizeY counting from left to right and from up to down.
    return (posX+1) + posY * matrixSizeX

def position_by_coordinates(posNumber : int, matrixSizeX : int):
    # Returns an x and y, this is done reversing the encoding done by position_by_counting
    y = ceil(posNumber / matrixSizeX)-1
    x = (posNumber - matrixSizeX * y)-1
    return y, x