from math import sqrt

def calculate_eigenvalues(a: list[list[float|int]]) -> list[float]:
	detA = a[0][0] * a[1][1] - a[0][1] * a[1][0]

	delta = (a[0][0] + a[1][1]) ** 2 - 4 * detA

	x1, x2 = ((a[0][0] + a[1][1]) + sqrt(delta)) / 2.0, ((a[0][0] + a[1][1]) - sqrt(delta)) / 2.0 

	return [max(x1, x2), min(x1, x2)]