import numpy as np

def compute_qkv(X, W_q, W_k, W_v):
    """Compute Query, Key, Value matrices from input X and weight matrices."""
    Q = np.dot(X, W_q)
    K = np.dot(X, W_k)
    V = np.dot(X, W_v)
    return Q, K, V

def softmax(e):
    exp_e = np.exp(e - np.max(e, axis=-1, keepdims=True))
    return exp_e / np.sum(exp_e, axis = -1, keepdims=True)

def self_attention(Q, K, V):
    """
    Compute scaled dot-product self-attention.
    
    Args:
        Q: Query matrix of shape (seq_len, d_k)
        K: Key matrix of shape (seq_len, d_k)
        V: Value matrix of shape (seq_len, d_v)
    
    Returns:
        Attention output of shape (seq_len, d_v)
    """
    # Your code here
    _, d_k = Q.shape

    A = Q @ K.T / np.sqrt(d_k)
    return softmax(A) @ V
