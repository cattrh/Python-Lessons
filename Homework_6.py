def find_min_max_rows(mat):
  rows = len(mat)
  cols = len(mat[0])
  min_row_index = 0
  max_row_index = 0
  min_sum = sum(mat[0])
  max_sum = sum(mat[0])
  for i in range(1, rows):
    row_sum = sum(mat[i])
    if row_sum < min_sum:
      min_row_index = i
      min_sum = row_sum
    if row_sum > max_sum:
      max_row_index = i
      max_sum = row_sum
  return min_row_index, max_row_index, min_sum, max_sum
mat = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
min_row_index, max_row_index, min_sum, max_sum = find_min_max_rows(mat)
print(f"Строка с наименьшей суммой элементов: {mat[min_row_index]}, сумма: {min_sum}")
print(f"Строка с наибольшей суммой элементов: {mat[max_row_index]}, сумма: {max_sum}")




def process_matrix(mat):
  rows = len(mat)
  cols = len(mat[0])
  for i in range(rows):
    min_index = 0
    min_value = mat[i][0]
    for j in range(1, cols):
      if mat[i][j] < min_value:
        min_index = j
        min_value = mat[i][j]
    if min_value % 2 == 0:
      mat[i][min_index] = 0
    else:
      mat[i][min_index] = 1
  return mat
mat = [
  [1.5, 3.2, 2.1],
  [4.7, 5.9, 1.3],
  [8.2, 7.6, 9.1]
]
new_mat = process_matrix(mat)
print("Начальная матрица:")
for row in mat:
  print(row)
print("\nИзмененная матрица:")
for row in new_mat:
  print(row)

