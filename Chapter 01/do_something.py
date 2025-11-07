# heavy_compute.py (CPU-intensive routine)
import math

def perform_computation(count, output_list):
    """
    Simulates a processor-heavy task by applying mathematical transformations
    and storing the results in a shared list.
    """
    for num in range(count):
        value = math.pow(math.sqrt(num), 2)  # intensive calculation
        output_list.append(value)
