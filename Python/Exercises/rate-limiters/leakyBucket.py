import time 
import threading
from collections import deque
class LeakyBucket:
    def __init__(self, capacity, outflow_rate):
        self.bucket = 0
        self.capacity = capacity
        self.last_leaked_time = time.time()
        self.outflow_rate = outflow_rate
        self.lock = threading.Lock()
    
    def _leak(self):
        now = time.time()
        elapsed = now - self.last_leaked_time
        leak = elapsed * self.outflow_rate
        with self.lock:
            self.bucket = max(0, self.bucket - leak)
            self.last_leaked_time = now
    
    def isAllowed(self):
        self._leak()
        if self.bucket < 0:
            return True
        else:
            return False
            
lb = LeakyBucket(4, 1)
for request in range(0,10):
    