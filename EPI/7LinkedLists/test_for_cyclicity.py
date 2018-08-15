# Solution


def is_cyclic(head):
    # Determines the distance from head to slow node
    def cycle_length(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step

    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            # New variable to go to the same node that slow is on
            cyclic_iterator = head
            for _ in range(cycle_length(slow)):
                cyclic_iterator = cyclic_iterator.next
            # Starts from the head and travels with cyclic_iterator. When they meet, that is the beginning of the
            # cycle
            cyclic_start = head
            while cyclic_start is not cyclic_iterator:
                cyclic_iterator = cyclic_iterator.next
                cyclic_start = cyclic_start.next
            return cyclic_start
    return None

