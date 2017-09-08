class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def __str__(self):
        return '%s' % self.data


class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    def find_nth_node_from_end(self, n):
        root = self.head
        root2 = self.head
        length = 0
        while root:
            length += 1
            root = root.getNext()
        if n > length or n < 0:
            return None
        for i in range(length - n):
            root2 = root2.getNext()
        return root2
