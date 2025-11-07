import multiprocessing
import time
from do_something import do_something

def execute_worker():
    proc_name = multiprocessing.current_process().name
    print(f"[🟢] Launching {proc_name}")

    results = multiprocessing.Manager().list()
    workload = 5 if proc_name == "daemon_worker" else 10
    do_something(workload, results)

    time.sleep(1)
    print(f"[✅] Shutting down {proc_name}")

def demonstrate_daemon_behavior():
    daemon_worker = multiprocessing.Process(name="daemon_worker", target=execute_worker)
    daemon_worker.daemon = True

    regular_worker = multiprocessing.Process(name="regular_worker", target=execute_worker)
    regular_worker.daemon = False

    daemon_worker.start()
    regular_worker.start()

    daemon_worker.join(timeout=2)
    regular_worker.join()

if __name__ == "__main__":
    demonstrate_daemon_behavior()
