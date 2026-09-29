import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A_arr, T_arr, S_arr = np.array(A, dtype=float), np.array(T, dtype=float), np.array(S, dtype=float)

	try:
		T_inv = np.linalg.inv(T)
		_ = np.linalg.inv(S)
		
		transformed_matrix = T_inv @ A @ S
	except:
		return -1
	
	return transformed_matrix.tolist()