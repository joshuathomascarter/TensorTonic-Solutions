import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a normalized NumPy array along the specified axis.
    Supports 'l1', 'l2', 'max' (L-infinity), and 'minmax' normalization.
    """
    X = np.array(matrix, dtype=float)
    norm_type_clean = norm_type.lower()
    
    # 1. Calculate the norm along specified axis using keepdims=True for broadcasting
    if norm_type_clean == "l1":
        norm = np.sum(np.abs(X), axis=axis, keepdims=True)
    elif norm_type_clean == "l2":
        norm = np.sqrt(np.sum(X**2, axis=axis, keepdims=True))
    elif norm_type_clean in ("max", "inf"):
        norm = np.max(np.abs(X), axis=axis, keepdims=True)
    elif norm_type_clean == "minmax":
        min_val = np.min(X, axis=axis, keepdims=True)
        max_val = np.max(X, axis=axis, keepdims=True)
        denom = np.where(max_val - min_val == 0.0, 1.0, max_val - min_val)
        return (X - min_val) / denom
    else:
        raise ValueError(f"Unsupported norm_type: '{norm_type}'. Choose 'l1', 'l2', 'max', or 'minmax'.")

    # 2. Safe division: replace 0-norm with 1.0 to prevent division-by-zero (NaNs)
    norm = np.where(norm == 0.0, 1.0, norm)

    # 3. Divide with automatic shape broadcasting
    return X / norm