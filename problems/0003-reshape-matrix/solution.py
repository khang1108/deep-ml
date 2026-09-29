import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	n, m = len(a), len(a[0])
	if n * m != new_shape[0] * new_shape[1]:
		return []

	reshaped_matrix = []
	flatten_matrix = []

	for i in range(n):
		for j in range(m):
			flatten_matrix.append(a[i][j])
	
	for i in range(new_shape[0]):
		new_row = []
		for j in range(new_shape[1]):
			new_row.append(flatten_matrix[i * new_shape[1] + j])
		reshaped_matrix.append(new_row)

	return reshaped_matrix