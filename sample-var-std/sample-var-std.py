import numpy as np

def sample_var_std(x: list) -> dict:
    n = len(x)
    mean = sum(x) / n
    
    # 1. Take every data point (xi), subtract the mean, and square it
    squared_diffs = [(xi - mean) ** 2 for xi in x]
    
    # 2. Sum those squared differences and divide by (n - 1)
    variance = sum(squared_diffs) / (n - 1)
    
    # 3. Take the square root for standard deviation
    standard_deviation = math.sqrt(variance)
    
    return {
        "variance": float(variance),
        "standard_deviation": float(standard_deviation)
    }