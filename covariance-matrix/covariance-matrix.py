import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    X_arr = np.array(X, dtype=float) 
    n_samples = X_arr.shape[0]

    X_centred = X_arr - np.mean(X_arr, axis=0)

    covariance_mat = (X_centred.T @ X_centred) / (n_samples-1)
    return covariance_mat