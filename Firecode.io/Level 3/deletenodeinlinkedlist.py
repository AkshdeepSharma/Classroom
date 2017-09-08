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

    # method for deleting a node having a certain data
    def delete(self, data):
        root = self.head
        while root.data != data:
            root = root.getNext()
        root2 = root.getNext()
        root.setNext(root2)
        return root