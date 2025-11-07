import threading
import time
from do_something import do_something

def task_handler(task_id, workload, result_list, reentrant_lock):
    print(f"[🧵] Task {task_id} started.")
    with reentrant_lock:
        # nested acquisition to illustrate reentrant behavior
        with reentrant_lock:
            do_something(workload, result_list)
    print(f"[✅] Task {task_id} completed.")

if __name__ == "__main__":
    result_list = []
    reentrant_lock = threading.RLock()
    thread_total = 3
    workload_size = 7

    thread_group = [
        threading.Thread(target=task_handler, args=(i, workload_size, result_list, reentrant_lock))
        for i in range(thread_total)
    ]

    for thread in thread_group:
        thread.start()
        time.sleep(0.5)
    for thread in thread_group:
        thread.join()

    print("\n[📦] Final Results:", result_list)
