class SinglyLinkedList:
    # constructor
    def __init__(self):
        self.head = None

    # method for setting the head of the Linked List
    def setHead(self, head):
        self.head = head

    # method for deleting a node having a certain data
    def delete(self, data):
        current = self.head
        previous = None
        if self.head is None:
            return None
        while current.data != data:
            previous = current
            current = current.getNext()
        if current == self.head and current.getNext is None:
            return 0
        elif current == self.head:
            self.head = current.getNext()
            current = None
        else:
            previous.setNext(current.getNext())
        return current
