class Queue(object):
    def __init__(self, max_size=20):
        self.queue = []
        self.size = 0
        self.max_size = max_size
        self.front = None
        self.rear = None

    def isFull(self):
        return self.size >= self.max_size

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.isFull():
            raise Exception('Overflow Error: Queue is full!')
        else:
            self.queue.append(item)

        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size   # Update index of last item

        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Underflow Error: Queue is empty!')
        else:
            self.queue.pop(0)
            self.size -= 1
            if self.isEmpty():
                self.front = self.rear = 0
            else:
                self.rear = self.size - 1

    def size(self):
        return self.size

    def front(self):
        return self.queue[self.front]

    def list(self):
        for i in self.queue:
            print(i)
