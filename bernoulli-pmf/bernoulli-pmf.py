import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    x_arr = np.array(x)

    pmf = np.array(np.where(x_arr == 1, p, 1 - p).tolist())

    
# Theoretical moments for a Bernoulli distribution
    mean = float(p)
    variance = float(round(p * (1 - p), 10))
    
    return {
        "pmf": pmf,
        "mean": mean,
        "variance": variance
    }