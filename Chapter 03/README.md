##  Python Multiprocessing: Hands-On Exploration

This section dives into Python’s `multiprocessing` module through practical examples that demonstrate how to launch, label, coordinate, monitor, and terminate multiple processes. All examples use a shared CPU-intensive function `do_something()` from `do_something.py`.

---

###  1. `naming_processes.py`  
**Objective:** Assign custom identifiers to processes and measure execution time.  
**Example:**
```python
multiprocessing.Process(name='worker_one', target=do_something, args=(1000, out_list1))
multiprocessing.Process(target=do_something, args=(1000, out_list2))
```
**Result:**  
- worker_one output size: 1000  
- unnamed process output size: 1000  
- Duration: 0.43 seconds  
**Takeaway:** Named and unnamed processes executed in parallel, improving performance over sequential runs.

---

###  2. `spawning_processes.py`  
**Objective:** Dynamically create multiple processes using a loop.  
**Example:**
```python
for i in range(6):
    multiprocessing.Process(target=myFunc, args=(i,)).start()
```
**Result:**  
Each process handled a workload of `i * 1000` independently.  
**Takeaway:** Demonstrated scalable parallelism with predictable output per worker.

---

###  3. `killing_processes.py`  
**Objective:** Showcase process lifecycle — starting, terminating, and joining.  
**Example:**
```python
p.start(); p.terminate(); p.join()
```
**Result:**  
- Process launched and terminated successfully  
- Exit status: 0  
**Takeaway:** Validated safe lifecycle handling using `.start()`, `.terminate()`, and `.join()`.

---

###  4. `run_background_processes_no_daemons.py`  
**Objective:** Contrast daemon and non-daemon process behavior.  
**Example:**
```python
background_process.daemon = True  
NO_background_process.daemon = False
```
**Result:**  
- Daemon exited with main program  
- Regular process completed and returned data  
**Takeaway:** Daemons are tied to the main thread’s lifespan; regular processes run independently.

---

###  5. `processes_barrier.py`  
**Objective:** Coordinate process execution using `Barrier` and `Lock`.  
**Example:**
```python
Barrier(2), Lock()
```
**Result:**  
Processes paused at the barrier and printed results in synchronized order.  
**Takeaway:** Barrier ensured alignment; Lock protected shared data access.

---

###  6. `process_pool.py`  
**Objective:** Use a process pool for efficient parallel computation.  
**Example:**
```python
pool.map(do_something, range(10))
```
**Result:**  
Computed squares: `[0, 1, 4, ..., 81]`  
**Takeaway:** Tasks were evenly distributed across 4 workers, maximizing CPU usage.

---

###  Summary Overview

| Script Name                          | Purpose                          | ✅ | Key Insight                                 |
|-------------------------------------|----------------------------------|----|---------------------------------------------|
| `naming_processes.py`               | Process labeling & timing        | ✅ | Easier debugging with named workers         |
| `spawning_processes.py`             | Loop-based process creation      | ✅ | Scalable and isolated execution             |
| `killing_processes.py`              | Start/stop/join demonstration    | ✅ | Controlled shutdown and cleanup             |
| `run_background_processes_no_daemons.py` | Daemon vs non-daemon         | ✅ | Daemons exit early; regulars complete tasks |
| `processes_barrier.py`              | Coordination with Barrier & Lock | ✅ | Ordered and safe execution                  |
| `process_pool.py`                   | Parallelism using Pool           | ✅ | Efficient task distribution                 |

---

###  Key Learnings

- Multiprocessing enables true parallel execution for CPU-bound workloads.  
- Naming processes improves traceability and debugging.  
- Daemon threads are short-lived; regular ones persist until completion.  
- Synchronization primitives like Barrier and Lock help manage concurrency safely.  
- Pools simplify task distribution across multiple workers.
