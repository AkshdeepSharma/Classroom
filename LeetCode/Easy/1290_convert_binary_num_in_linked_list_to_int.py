# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        binary_list = []
        while head:
            binary_list.append(str(head.val))
            head = head.next
        binary = "".join(binary_list)
        return int(binary, 2)
