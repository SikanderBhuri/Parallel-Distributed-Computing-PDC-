import threading
import time
from do_something import do_something

def thread_task(task_id, workload, result_store, mutex):
    print(f"[🧵] Task {task_id} has started.")
    with mutex:
        do_something(workload, result_store)
    print(f"[✅] Task {task_id} has completed.")

if __name__ == "__main__":
    result_store = []
    mutex = threading.Lock()

    thread_count = 3
    workload = 7

    thread_pool = [
        threading.Thread(target=thread_task, args=(i, workload, result_store, mutex))
        for i in range(thread_count)
    ]

    for thread in thread_pool:
        thread.start()
        time.sleep(0.5)  # slight delay for clearer output sequence

    for thread in thread_pool:
        thread.join()

    print("\n[📦] Final Results:", result_store)
    print("[📏] Total Items (Lock):", len(result_store))
