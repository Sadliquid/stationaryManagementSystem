# Name: Joshua Long Yu Xuan
# Student Admin Number: 230627W
# Tutorial Group: IT2153-01

class RestockingQ:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []
    
    def len(self):
        return len(self.queue)
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty. Nothing to dequeue."
        else:
            return self.queue.pop(0)