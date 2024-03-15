# Многомерные списки

# Двумерный список - это последовательность одномерных списков
# Трехмерный список - это список двумерных списков

# ОБЪЯВЛЕНИЕ ДВУМЕРНОГО СПИСКА: 

arr_2d = [[1,2,3], [4,5,6], [7,8,9]]
print(arr_2d)

for elem in arr_2d: 
    print(*elem)

print(arr_2d[2][2])

# !!! В Python вложенные массивы могут содержать разное количество элементов: 
arr_2d = [[1,2,3], [1,2,4,5,6], [7,8,9,10]]
for elem in arr_2d: 
    print(*elem)

# Реализуем красивый вывод на экран двумерного массива: 

def print_matrix (arr_2d) : 
    for elem in arr_2d: 
        print(*elem)

# Задача: реализовать двумерный список с m строками и n столбцами, у которой все значения равны 0, 
# и вернуть ее в качестве возвращаемого значения метода create_2D_array
        
def create_2D_array (m, n) : 
    result = []
    for i in range(m) : 
        raw = []
        for j in range(n) : 
            raw.append(0)
        result.append(raw)
    return result

print_matrix(create_2D_array(2,3))

# Задача: зеркально отобразить матрицу относительно вертикальной оси, то есть, перевернуть строки в ней. 

def mirrow_reflection (matrix) : 
    for i in range(len(matrix)) : 
        for j in range(len(matrix[i])//2) : 
            matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
    return matrix

matrix = [[1,2,3,4,5,6,7], [2,3,4,5,6,7,8], [3,4,5,6,7,8,9], [4,5,6,7,8,9,10]]
print_matrix(mirrow_reflection(matrix))
