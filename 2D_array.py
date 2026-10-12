
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])  # Output: 1

for row in matrix:
    for column in row:
        print(column)
    print(row)