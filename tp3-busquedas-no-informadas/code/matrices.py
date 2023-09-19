# Module to create and show matrices easily

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
            