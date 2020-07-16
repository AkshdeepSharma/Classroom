# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1, n2 = self.getNumFromLinkedList(l1), self.getNumFromLinkedList(l2)
        n3 = str(n1 + n2)
        head = ListNode()
        dummy = head
        for i in range(len(n3)):
            dummy.val = int(n3[i])
            if i != len(n3) - 1:
                dummy.next = ListNode()
                dummy = dummy.next
        return head

    def getNumFromLinkedList(self, l1):
        num = 0
        while l1:
            num *= 10
            num += l1.val
            l1 = l1.next
        return num
