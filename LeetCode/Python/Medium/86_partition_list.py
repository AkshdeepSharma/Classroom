# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        nodes = []
        dummy = head
        last = None
        while dummy:
            if dummy.val < x:
                if last is None:
                    last = dummy
                    head = last
                else:
                    last.next = dummy
                    last = dummy
            else:
                nodes.append(dummy)
            dummy = dummy.next
        if last is None or not nodes:
            return head
        for node in nodes:
            last.next = node
            last = last.next
        last.next = None
        return head
