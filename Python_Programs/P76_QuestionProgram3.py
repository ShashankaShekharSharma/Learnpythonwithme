#A Square matrix M is said to be:
#Diagonal: if the entries outside the main diagonals are all zeros
#Scaler: if it is a diagonal matrix, all of whose diagonal elements are equal
#Identity: if it is a scaler matrix, all of whose diagonal elements are equal to 1
#Write a function name matrix_type that accepts a matrix M as an argument and returns the type of the matrix. It should be one of these strings: diagonal, scaler, identity and non diagonal. The type you output should be the most appropiate one for the given matrix.
#You do not have to accept the input from the user and print output to the console. You just have to write the function definitoon
def matrix(M):
    B = M[0][0]
    identity = 0
    scaler = 0
    for i in range(len(M)):
        for j in range(len(M)):
            if i != j:
                if M[i][j] != 0:
                    return "Non Diagonal"
        else:
            if M[i][j] == 1:
                identity += 1
            else:
                if M[i][j] == B:
                    scaler += 1
    if identity == len(M):
        return "Identity"
    else:
        if scaler==len(M):
            return "Scaler"
        else:
            return "Diagonal"