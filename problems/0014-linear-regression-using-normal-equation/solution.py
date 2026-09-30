import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	try: 
		X_arr = np.array(X, dtype=float)
		y_arr = np.array(y, dtype=float)

		X_T = X_arr.T
		theta = np.linalg.inv(X_T @ X) @ X_T @ y_arr
	except:
		return []
	return theta