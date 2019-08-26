class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.stack = [[]]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        stacked = False
        for i in range(len(self.stack)):
            if len(self.stack[i]) < self.capacity:
                self.stack[i].append(val)
                stacked = True
                break
        if not stacked:
            self.stack.append([val])

    def pop(self):
        """
        :rtype: int
        """
        if self.stack:
            ans = self.stack[-1].pop()
            if not self.stack[-1]:
                self.stack.pop()
            return ans
        else:
            return -1

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if 0 <= index < len(self.stack) and self.stack[index]:
            ans = self.stack[index].pop()
            if not self.stack[index]:
                self.stack.pop(index)
            return ans
        else:
            return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)

#FAILS SOME TEST CASES STILL WORKING ON IT