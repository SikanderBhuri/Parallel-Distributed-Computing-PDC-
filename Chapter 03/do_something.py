# core_task.py (CPU-intensive routine)
import math

def perform_task(count, output):
    """
    Simulates a CPU-bound operation by applying mathematical transformations
    and storing the results in a shared list.
    """
    for number in range(count):
        computed = math.pow(math.sqrt(number), 2)  # heavy computation simulation
        output.append(computed)
