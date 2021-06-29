from queue import Queue

# Initializing a queue
q = Queue(maxsize=3)

# return max size of queue
print(q.qsize())

# Adding of element
q.put('a')
q.put('b')
q.put('c')

# Return Boolean for Full
print("\nFull: ", q.full())

# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

# Return Boolean for Empty
print("\nEmpty: ", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())
