from P56_MatrixAddition import input_matrix  # Assuming you have the correct module for input_matrix

def matrix_multiplication(matrix1, matrix2):
    result = []

    if len(matrix1[0]) != len(matrix2):
        return "Matrix Multiplication is not possible"

    # Initialize the result matrix with zeros
    for i in range(len(matrix1)):
        result.append([0] * len(matrix2[0]))

    # Perform matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

print("Enter details for the first matrix:")
matrix1 = input_matrix()
print("\nEnter details for the second matrix:")
matrix2 = input_matrix()

result = matrix_multiplication(matrix1, matrix2)

if result != "Matrix Multiplication is not possible":
    print("\nResultant Matrix:")
    for row in result:
        print(row)
else:
    print(result)
