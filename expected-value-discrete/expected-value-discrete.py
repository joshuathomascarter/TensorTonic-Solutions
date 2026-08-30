import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    expected_value = np.sum(np.array(x) * np.array(p))
    return float(expected_value)