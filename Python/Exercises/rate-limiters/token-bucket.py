import time
import threading


class TockenBucket:
    def __init__(self, capacity, refill_rate ):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.last_refill_time = time.time()
        self.tokens = capacity
        self.lock = threading.Lock()
    
    def _refill(self):
        current_time = time.time()
        # print(self.tokens)
        elapsed = current_time - self.last_refill_time
        # print(type(elapsed))
        added = (elapsed / 60) * self.refill_rate
        if added > 0:
            self.tokens = min(self.capacity, self.tokens + added ) 
            self.last_refill_time = current_time
    
    def allowRequest(self):
        with self.lock:
            self._refill()
            print(self.tokens)
            if self.tokens >= 1:
                self.tokens -= 1
                return True
            else:
                return False
            
ratelimiter = TockenBucket(4, 2)
while True:
#   print(i)
  time.sleep(10)
  print(ratelimiter.allowRequest())