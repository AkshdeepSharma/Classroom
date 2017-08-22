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


class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    # method for inserting a new node at the end of a Linked List
    def insertAtEnd(self, data):
        new_node = Node()
        new_node.setData(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(new_node)