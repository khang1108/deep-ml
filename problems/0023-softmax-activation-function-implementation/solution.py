import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    scores_arr = np.array(scores, dtype=float)
    exp_e = np.exp(scores_arr - np.max(scores_arr, axis=-1, keepdims=True))
    return exp_e / np.sum(exp_e, axis=-1, keepdims=True)