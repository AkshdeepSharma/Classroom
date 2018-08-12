
def merge_sorted_lists(L1, L2):
    # Creates a new tail and head
    tail = new_head = ListNode()

    while L1 and L2:
        # Appends L1 node if smaller than L2 node and increments to next node
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        # Appends L2 node if smaller than L1 node and increments to next node
        else:
            tail.next = L2
            L2 = L2.next
        # Increments to next node so you don't overlap nodes
        tail = tail.next
    # Adds remaining nodes from L1 if L2 is null and vice versa
    tail.next = L1 or L2
    # Returns new list head
    return new_head.next

