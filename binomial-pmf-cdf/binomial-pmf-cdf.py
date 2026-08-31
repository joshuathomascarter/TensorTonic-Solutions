import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf without using nested or helper functions.
    """
    # PMF: P(X = k)
    pmf = math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    
    # CDF: P(X <= k) = sum of P(X = i) for i from 0 to k
    cdf = sum(math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i)) for i in range(k + 1))

    return {
        "pmf": float(round(pmf, 10)),
        "cdf": float(round(cdf, 10))
    }