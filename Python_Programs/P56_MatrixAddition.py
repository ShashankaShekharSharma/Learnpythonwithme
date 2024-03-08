def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices must have the same dimensions for addition.")
        return None
    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result_matrix.append(row)
    return result_matrix
def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter element at position ({i + 1}, {j + 1}): "))
            row.append(element)
        matrix.append(row)    
    return matrix
def main():
    print("Enter details for the first matrix:")
    matrix1 = input_matrix()
    print("\nEnter details for the second matrix:")
    matrix2 = input_matrix()
    result = matrix_addition(matrix1, matrix2)
    if result:
        print("\nResultant Matrix:")
        for row in result:
            print(row)
