from collections import deque

class RecentCounter(object):
    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        range_of_t = (t - 3000, t)
        self.queue.append(t)
        count = 0
        new_queue = deque()
        count = 0

        while self.queue:
            item = self.queue.popleft()
            if range_of_t[0] <= item <= range_of_t[1]:
                count += 1
                new_queue.append(item)

        self.queue = new_queue

        return count

