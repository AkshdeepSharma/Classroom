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

    # Method for inserting a new node at the start of a Linked List
    def insert_at_pos(self,data,pos):
        new_node = Node()
        new_node.setData = data
        if self.head is None:
            self.head = new_node
            return self.head
        current = self.head
        next = current.getNext()
        for i in range(pos - 1):
            current = next
            next = current.getNext()
        current.setNext(new_node)
        current = current.getNext()
        current.setNext(next)

'''
def insert_at_pos(self, data, pos):
    new_node = Node()
    new_node.setData(data)
    
    if self.head is None:
        self.head = new_node
    elif pos == 1:
        new_node.setNext(self.head)
        self.head = new_node
    else:
        current = self.head
        prev = None
        count = 1
        while current is not None:
            if count == pos:
                break;
            prev = current
            current = current.getNext()
            count += 1
        prev.setNext(new_node)
        new_node.setNext(current)

'''
