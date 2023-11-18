# This program calculates the determinant of a 2x2 matrix entered by the user.

# Function that calculates the determinant of a 2x2 matrix 
def determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

# Create a 2x2 matrix filled with zeros
matrix = [[0 for _ in range(2)] for _ in range(2)]

# Get input for each element in the matrix
for i in range(2):
    for j in range(2):
        matrix[i][j] = int(input(f"Enter integer value at position [{i}][{j}]: "))

# Display the matrix
print("\nThe matrix: ")
for row in matrix:
    print(row)

# Calculate and display the determinant
print(f"\nThe determinant of the matrix is {determinant(matrix)}")
