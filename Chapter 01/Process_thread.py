from do_something import *
import time
import multiprocessing
import threading

def run_multiprocessing(workload, num_workers):
    shared_output = multiprocessing.Manager().list()
    processes = []

    start = time.time()
    for _ in range(num_workers):
        proc = multiprocessing.Process(target=do_something, args=(workload, shared_output))
        processes.append(proc)

    for proc in processes:
        proc.start()
    for proc in processes:
        proc.join()
    end = time.time()

    print("[🔁] Multiprocessing finished.")
    print(f"[⏱️] Duration: {end - start:.4f} seconds")

def run_multithreading(workload, num_threads):
    thread_output = []
    threads = []

    start = time.time()
    for _ in range(num_threads):
        thread = threading.Thread(target=do_something, args=(workload, thread_output))
        threads.append(thread)

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end = time.time()

    print("[🔁] Multithreading finished.")
    print(f"[⏱️] Duration: {end - start:.4f} seconds")

if __name__ == "__main__":
    TASK_SIZE = 1000
    PROCESS_COUNT = 50
    THREAD_COUNT = 50

    run_multiprocessing(TASK_SIZE, PROCESS_COUNT)
    run_multithreading(TASK_SIZE)
