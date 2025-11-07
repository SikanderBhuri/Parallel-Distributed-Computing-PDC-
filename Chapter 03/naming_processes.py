import multiprocessing
import time
from do_something import do_something

def execute_parallel_tasks(workload):
    results_a = multiprocessing.Manager().list()
    results_b = multiprocessing.Manager().list()

    process_a = multiprocessing.Process(
        name="Processor-A",
        target=do_something,
        args=(workload, results_a)
    )

    process_b = multiprocessing.Process(
        target=do_something,
        args=(workload, results_b)
    )

    start_time = time.time()
    process_a.start()
    process_b.start()

    process_a.join()
    process_b.join()
    end_time = time.time()

    return results_a, results_b, end_time - start_time

if __name__ == "__main__":
    WORKLOAD_SIZE = 1000
    output_a, output_b, elapsed = execute_parallel_tasks(WORKLOAD_SIZE)

    print(f"[🧮] Processor-A result count: {len(output_a)}")
    print(f"[🧮] Processor-B result count: {len(output_b)}")
    print(f"[⏱️] Total runtime: {elapsed:.2f} seconds")
