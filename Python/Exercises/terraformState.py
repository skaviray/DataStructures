from threading import Lock
class TerraformState:
    def __init__(self):
        self.state = None
        self.lock = None

    def lockState(self):
        self.lock = Lock()
        return self.lock.
    
    def unlock(self):
        self.lock = None
    
    def setState(self, state):
        if self.lock:
            raise Exception("state is already locked..")
        else:
            self.state = state

    def getState(self, state):
        return self.state
    
state = TerraformState()

# state.lockState()
# state
state.setState("state is hello")
