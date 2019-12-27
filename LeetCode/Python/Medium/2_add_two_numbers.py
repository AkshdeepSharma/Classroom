# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = [], []
        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
            num1[i] = str(num1[i])
        for i in range(len(num2)):
            num2[i] = str(num2[i])
        num3 = list(str(int("".join(num1)) + int("".join(num2))))[::-1]
        head = dummy_head = ListNode(num3[0])
        for i in range(1, len(num3)):
            new_node = ListNode(num3[i])
            head.next = new_node
            head = head.next
        return dummy_head
