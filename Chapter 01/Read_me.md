##  Python Parallelism: Comparing Multiprocessing and Multithreading

This study evaluates the performance of Python’s `multiprocessing` and `threading` modules by executing the same computational routine (`do_something`) under varying concurrency models. The goal is to determine which strategy yields better efficiency for a fixed workload and understand the reasons behind the performance differences.

---

###  Test Configuration

- **Language**: Python 3  
- **Modules Used**: `multiprocessing`, `threading`, `time`  
- **Task Size**: 1000 iterations per worker  
- **Platform**: Windows 10  

The function under test performs repeated mathematical operations (square root followed by exponentiation) and stores the results in a shared list.

---

### Execution Scenarios

We ran the function using both threads and processes across three concurrency levels:

| Configuration           | Multiprocessing Time | Multithreading Time |
|-------------------------|----------------------|----------------------|
| 5 Workers               | 1.428 seconds        | 0.044 seconds        |
| 10 Workers              | 2.438 seconds        | 0.041 seconds        |
| 50 Workers              | 8.716 seconds        | 0.099 seconds        |

---

###  Interpretation

- **Multithreading consistently outperformed multiprocessing** for the given workload.
- The `do_something` function simulates an **I/O-bound task** (e.g., includes `time.sleep()`), which favors threading.

#### Why Threads Win for I/O-Bound Work:
- Threads can continue execution while others wait, maximizing CPU usage.
- Python’s **Global Interpreter Lock (GIL)** doesn’t hinder performance in I/O-heavy scenarios.

#### Why Processes Lag:
- Each process runs in its own memory space, introducing overhead.
- Inter-process communication and context switching slow things down.
- For lightweight tasks, the cost of spawning processes outweighs the benefits.

---

###  Conclusion

- **Use threads** for I/O-bound workloads like file access, network calls, or delays.
- **Use processes** for CPU-heavy tasks like number crunching, image processing, or model training.

In this benchmark, multithreading was clearly the more efficient choice for the simulated I/O-bound workload.

---

###  Running the Demo

To try it yourself:

```bash
git clone <your-repo-url>
cd <repo-folder>
python Process_thread.py
