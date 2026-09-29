def transpose_matrix(matrix: list[list[float]]) -> list[list[float]]:
	n, m = len(matrix), len(matrix[0])
	ret = []

	for j in range(m):
		new_row = []
		for i in range(n):
			new_row.append(matrix[i][j])
		ret.append(new_row)

	return ret

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'column':
		matrix = transpose_matrix(matrix)
	n, m = len(matrix), len(matrix[0])

	means = []
	for i in range(n):
		curSum = 0.0
		for j in range(m):
			curSum += matrix[i][j]
		means.append((float)(curSum / m))

	return means