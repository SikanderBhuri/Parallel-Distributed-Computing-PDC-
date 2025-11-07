import threading
import time
from do_something import do_something

def task_executor(task_id, workload, result_list, gate):
    print(f"[⏳] Task {task_id} is waiting for access...")
    with gate:
        print(f"[🚀] Task {task_id} is now running.")
        do_something(workload, result_list)
        print(f"[✅] Task {task_id} has completed.")

if __name__ == "__main__":
    result_list = []
    gate = threading.Semaphore(2)  # limit: 2 threads at a time
    total_threads = 3
    workload_size = 7

    thread_pool = [
        threading.Thread(target=task_executor, args=(i, workload_size, result_list, gate))
        for i in range(total_threads)
    ]

    for thread in thread_pool:
        thread.start()
    for thread in thread_pool:
        thread.join()

    print("\n[📦] Aggregated Results:", result_list)
    print("[📏] Total Items (Semaphore):", len(result_list))
