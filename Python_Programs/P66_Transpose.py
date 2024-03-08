from P56_MatrixAddition import input_matrix
def transpose(matrix):
    result_matrix = []
    for i in range(len(matrix[0])):
        new_row=[]
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        result_matrix.append(new_row)
    return result_matrix

matrix = input_matrix()
print("Original Matrix: ")
for row in matrix:
    print(row)
print("Transpose of the matrix is: ")
for row in transpose(matrix):
    print(row)