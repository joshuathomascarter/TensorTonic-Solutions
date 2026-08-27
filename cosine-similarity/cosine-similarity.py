import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a = np.asarray(a, dtype = float)
    b = np.asarray(b, dtype = float)
    result = float(np.dot(a, b))


    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)

    if ((a_norm and a_norm) == 0):
        return float(0)
    else: 
        return float(result / (a_norm * b_norm))