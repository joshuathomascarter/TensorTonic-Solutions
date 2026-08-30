from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    counts = Counter(x)
    max_count = max(counts.values())
        
        # Creating and naming the required dictionary
    stats_dict = {
            "mean": float(np.mean(x)),
            "median": float(np.median(x)),
            # Extracting the first mode from the list comprehension
            "mode": float([num for num, freq in counts.items() if freq == max_count][0])
    }
        
    return stats_dict

