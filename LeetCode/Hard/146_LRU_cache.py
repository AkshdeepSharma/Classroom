class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = "#", "$"  # Dummy head and tail
        self.next, self.prev = {}, {}
        self.connect(self.head, self.tail)  # Doubly connects head and tail

    def connect(self, a, b):
        self.next[a], self.prev[b] = b, a  # Links 2 nodes together

    def delete(self, key):
        self.connect(self.prev[key], self.next[key])  # Creates connections between deleted nodes prev and next nodes
        del self.prev[key], self.next[key], self.cache[key]  # Deletes connections between deleted nodes prev and next nodes

    def append(self, key, val):
        self.cache[key] = val
        self.connect(self.prev[self.tail], key)  # Adds new node to end of list
        self.connect(key, self.tail)  # Adds new node to end of list
        if len(self.cache) > self.capacity:  # Evicts least used node
            self.delete(self.next[self.head])

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.delete(key)
        self.append(key, val)
        return val

    def put(self, key, val):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.delete(key)
        self.append(key, val)
