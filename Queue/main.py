from Queue.python_queue import Queue

if __name__ == '__main__':

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print("List Items ::")
    queue.list()
    print("Size of Queue :: {}".format(queue.size))
    print("====== Remove Operation =====")
    queue.dequeue()
    queue.dequeue()
    print("List Items After Dequeue Operation ::")
    queue.list()
    print("Size of Queue After Dequeue Operation :: {}".format(queue.size))
