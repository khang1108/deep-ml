def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	n, m = len(matrix), len(matrix[0])
	for i in range(n):
		for j in range(m):
			matrix[i][j] *= scalar
	return matrix