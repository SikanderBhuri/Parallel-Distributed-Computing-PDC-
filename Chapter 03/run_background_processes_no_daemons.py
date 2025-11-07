import multiprocessing
import time
from do_something import do_something

def task_handler():
    proc_name = multiprocessing.current_process().name
    print(f"[🟢] Launching {proc_name}\n")

    if proc_name == 'background_process':
        for count in range(5):
            print(f"[➡️] Step {count}\n")
        time.sleep(1)
    else:
        output = []
        do_something(3, output)  # ✅ correct argument passing
        print(f"[📊] Computation results: {output}")
        time.sleep(1)

    print(f"[🔚] Shutting down {proc_name}\n")

if __name__ == '__main__':
    daemon_task = multiprocessing.Process(
        name='background_process', target=task_handler)
    daemon_task.daemon = False

    regular_task = multiprocessing.Process(
        name='NO_background_process', target=task_handler)
    regular_task.daemon = False

    daemon_task.start()
    regular_task.start()
