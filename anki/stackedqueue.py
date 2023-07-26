class FastQueue:
    def __init__(self):
        self.en = []
        self.de = []

    def enqueue(self, item):
        self.en.append(item)

    def dequeue(self):
        if len(self.de) == 0:
            if len(self.en) == 0:
                return
            while self.en:
                self.de.append(self.en.pop())
        return self.de.pop()
