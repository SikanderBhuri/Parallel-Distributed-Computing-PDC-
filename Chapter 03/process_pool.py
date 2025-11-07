import multiprocessing
from do_something import do_something

def transform_value(x):
    buffer = []
    do_something(2, buffer)  # simulate CPU work
    return x ** 2

def parallel_executor(data_set, worker_count):
    with multiprocessing.Pool(processes=worker_count) as executor:
        results = executor.map(transform_value, data_set)
    return results

if __name__ == "__main__":
    DATA = list(range(10))
    WORKERS = 4

    final_output = parallel_executor(DATA, WORKERS)
    print("[📊] Computed Squares:", final_output)
