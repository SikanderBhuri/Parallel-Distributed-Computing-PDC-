import threading
import time
from do_something import do_something

def task_runner(task_id, workload, result_list, sync_flag):
    print(f"[🧵] Task {task_id} initiated.")
    do_something(workload, result_list)
    with sync_flag:
        print(f"[📣] Task {task_id} signaling monitor.")
        sync_flag.notify()
    print(f"[✅] Task {task_id} completed.")

def observer(result_list, sync_flag, expected_count):
    with sync_flag:
        while len(result_list) < expected_count:
            sync_flag.wait()
            print(f"[🔍] Observer: current size = {len(result_list)}")

if __name__ == "__main__":
    results = []
    sync_flag = threading.Condition()
    thread_count = 3
    workload_size = 7
    expected_total = thread_count * workload_size

    workers = [
        threading.Thread(target=task_runner, args=(i, workload_size, results, sync_flag))
        for i in range(thread_count)
    ]
    observer_thread = threading.Thread(target=observer, args=(results, sync_flag, expected_total))

    observer_thread.start()
    for worker in workers:
        worker.start()
        time.sleep(0.5)
    for worker in workers:
        worker.join()
    observer_thread.join()

    print("\n[📦] Final Results:", results)
    print("[📏] Total Entries (Condition):", len(results))
