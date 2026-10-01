import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	probabilities = []
	for x in features:
		z = bias
		for i, x_i in enumerate(x):
			w_i = weights[i]
			z = z + w_i * x_i
		sigmoid_val = 1.0 /(1.0 + math.exp(-z))
		prob_val = round(sigmoid_val, 4)
		probabilities.append(prob_val)

	mse = 0.0
	for i, prob in enumerate(probabilities):
		mse += (prob - labels[i]) ** 2
	mse = mse / len(probabilities)

	return probabilities, mse