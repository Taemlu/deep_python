# Напишите функцию для транспонирования матрицы.

def transpose_matrix(lst: list) -> list:
    return [list(lst) for lst in zip(*lst)]


matrix = [[3, 2, 32, 20],
          [9, 5, 88, 21],
          [11, 89, 9, 5422]]

new_matrix = transpose_matrix(matrix)

print(*matrix, sep='\n')
print()
print(*new_matrix, sep='\n')
