import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime
from do_something import do_something

def synchronized_worker(barrier, mutex):
    proc_name = multiprocessing.current_process().name
    barrier.wait()
    current_time = datetime.fromtimestamp(time())
    with mutex:
        print(f"[🔒] {proc_name} triggered at {current_time}")
        results = []
        do_something(2, results)
        print(f"[📊] {proc_name} output: {results}")

def unsynchronized_worker():
    proc_name = multiprocessing.current_process().name
    current_time = datetime.fromtimestamp(time())
    print(f"[⏱️] {proc_name} triggered at {current_time}")
    results = []
    do_something(2, results)
    print(f"[📊] {proc_name} output: {results}")

def initiate_processes():
    barrier = Barrier(2)
    mutex = Lock()

    task_list = [
        Process(name="Worker-A (barrier)", target=synchronized_worker, args=(barrier, mutex)),
        Process(name="Worker-B (barrier)", target=synchronized_worker, args=(barrier, mutex)),
        Process(name="Worker-C (no barrier)", target=unsynchronized_worker),
        Process(name="Worker-D (no barrier)", target=unsynchronized_worker),
    ]

    for task in task_list:
        task.start()

if __name__ == "__main__":
    initiate_processes()
