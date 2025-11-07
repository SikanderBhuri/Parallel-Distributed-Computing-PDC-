# compute_heavy.py (CPU-intensive simulation)
import math

def compute_heavy(iterations, results):
    """
    Emulates a processor-intensive loop by applying mathematical transformations
    and collecting the output in a shared list.
    """
    for value in range(iterations):
        transformed = math.pow(math.sqrt(value), 2)
        results.append(transformed)
