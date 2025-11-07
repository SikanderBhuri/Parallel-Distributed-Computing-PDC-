#  Python Thread Synchronization Techniques  
### (Using Lock, RLock, Semaphore, and Condition)

This module showcases how various synchronization primitives from Python’s `threading` library manage concurrent access to shared data. Each example leverages a common computational routine from `do_something.py` to simulate workload and demonstrate thread-safe behavior.

---

##  Mechanisms Explored

### 1.  Lock  
**Function**: Ensures exclusive access to shared resources — only one thread can modify `out_list` at a time.

**Execution Snapshot**:
```
Thread 0 started.  
Thread 0 finished.  
Thread 1 started.  
Thread 1 finished.  
Thread 2 started.  
Thread 2 finished.  
Length of list (Lock): 21
```

**Outcome**: Data integrity preserved; expected output size confirmed.

---

### 2.  RLock (Reentrant Lock)  
**Function**: Allows the same thread to acquire the lock multiple times without deadlock.

**Execution Snapshot**:  
Similar to Lock — threads complete sequentially with consistent results.

**Outcome**: Reliable access and correct output; total list length = 21.

---

### 3.  Semaphore  
**Function**: Restricts the number of threads that can access a resource simultaneously.

**Execution Snapshot**:
```
Thread 0 waiting for permit...  
Thread 0 started.  
Thread 1 waiting for permit...  
Thread 2 waiting for permit...  
Thread 1 started.  
Thread 0 finished.  
Thread 1 finished.  
Thread 2 started.  
Thread 2 finished.  
Length of list (Semaphore): 21
```

**Outcome**: Controlled concurrency; output remains accurate.

---

### 4.  Condition  
**Function**: Enables threads to wait for a signal before proceeding — ideal for coordination.

**Execution Snapshot**:
```
Thread 0 notifying condition.  
Thread 1 notifying condition.  
Thread 2 notifying condition.  
Monitor: Current length = 7  
Monitor: Current length = 14  
Monitor: Current length = 21
```

**Outcome**: Threads communicate progress; monitor tracks shared state effectively.

---

##  Comparison Summary

| Sync Primitive | Role in Concurrency               | Behavior Style           | Thread Safety | Ideal Use Case                  |
|----------------|-----------------------------------|---------------------------|---------------|----------------------------------|
| Lock           | Basic mutual exclusion            | Sequential thread access  | ✅             | General thread protection        |
| RLock          | Recursive locking                 | Similar to Lock           | ✅             | Nested lock scenarios            |
| Semaphore      | Limited parallel access           | Batched execution         | ✅             | Resource pool management         |
| Condition      | Event-based coordination          | Signal-driven progression | ✅             | Producer-consumer workflows      |

---

##  Final Thoughts

Each synchronization method effectively protected shared data and avoided race conditions.  
- **Lock/RLock**: Best for simple mutual exclusion.  
- **Semaphore**: Ideal when limiting concurrent access to a resource.  
- **Condition**: Useful for coordinating thread behavior based on state changes.

Choose the right tool based on your concurrency model and resource constraints.

---

##  Execution Guide

Run each script individually to observe synchronization in action:
```bash
python Chapter_02/Lock.py
python Chapter_02/RLock.py
python Chapter_02/Semaphore.py
python Chapter_02/Condition.py
