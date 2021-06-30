class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def add_item(self, item):

        self.node = Node(item)

        if self.head == None:
            self.head = self.node
            return

        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.node
        self.length += 1

    def remove_item(self):
        if self.length <= 0 or self.head == None:
            return

        current = self.head
        previous = self.head
        while current.next != None:
            previous = current
            current = current.next

        previous.next = None
        self.length -= 1

    def delete_list(self):
        self.head = None

    def count(self):
        return self.length

    def find(self, n):
        if self.length <= 0 or self.head == None or n > self.length:
            return None

        current = self.head
        for i in range(0, self.length - n):
            current = current.next

        return current.data

    def list_items(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next
