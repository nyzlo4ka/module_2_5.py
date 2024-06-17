def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


result1 = get_matrix(2, 4, 99)
result2 = get_matrix(3, 5, 66)
result3 = get_matrix(4, 6, 3)
print(result1)
print(result2)
print(result3)
