class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack1 and not self.stack2:
            return None
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()
    
    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
    