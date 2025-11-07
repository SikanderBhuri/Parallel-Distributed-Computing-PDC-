import multiprocessing
import time
from do_something import do_something

def execute_job():
    shared_list = multiprocessing.Manager().list()
    print("[🟢] Job initiated")
    do_something(10, shared_list)
    print(f"[✅] Job completed with {len(shared_list)} entries")

def observe_process(worker):
    print("[🔍] Initial state:", worker, worker.is_alive())
    worker.start()
    print("[⚙️] Active state:", worker, worker.is_alive())
    time.sleep(2)
    worker.terminate()
    print("[🛑] Termination triggered:", worker, worker.is_alive())
    worker.join()
    print("[🔚] Post-join state:", worker, worker.is_alive())
    print("[📤] Final exit code:", worker.exitcode)

if __name__ == "__main__":
    job_process = multiprocessing.Process(target=execute_job)
    observe_process(job_process)
