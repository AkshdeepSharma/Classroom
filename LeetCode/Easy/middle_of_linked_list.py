# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        len_linked_list = 0
        curr = head
        while curr:
            curr = curr.next
            len_linked_list += 1

        curr = head
        len_linked_list = (len_linked_list) // 2
        for i in range(len_linked_list):
            curr = curr.next
        return curr