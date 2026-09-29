import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	A = np.array(A, dtype=float)
	B = np.array(b, dtype=float)
	
	nums = len(B)
	x = np.zeros(nums)

	while n:
		x_new = np.zeros(nums)
		
		for i in range(nums):
			cur_sum = 0
			for j in range(nums):
				if i != j:
					cur_sum += A[i][j] * x[j]
			x_new[i] = 1.0 / A[i][i] * (b[i] - cur_sum)

		x = x_new
		n -= 1
	return x.tolist()