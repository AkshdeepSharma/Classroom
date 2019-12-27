# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        to_skip = curr = head
        for i in range(n):
            to_skip = to_skip.next
        if not to_skip:
            return head.next
        while to_skip.next:
            curr = curr.next
            to_skip = to_skip.next
        curr.next = curr.next.next
        return head