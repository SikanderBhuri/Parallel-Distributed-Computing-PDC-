import multiprocessing
from do_something import do_something

def execute_worker(worker_id):
    print(f"[🔧] Worker {worker_id} initiated")
    results = multiprocessing.Manager().list()
    do_something(worker_id * 1000, results)
    print(f"[✅] Worker {worker_id} completed with {len(results)} entries")

def start_workers():
    for worker_num in range(6):
        process = multiprocessing.Process(target=execute_worker, args=(worker_num,))
        process.start()
        process.join()

if __name__ == "__main__":
    start_workers()
