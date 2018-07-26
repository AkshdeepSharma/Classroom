import collections


def generate_ip_address(input):
    class IpLevelNode:
        def __init__(self, level, ip_to_append, predecessor, successor):
            self.level = level
            self.ip_to_append = ip_to_append
            self.successor = successor
            if level == 0:
                self.predecessor = ip_to_append
            else:
                self.predecessor = str(predecessor) + '.' + str(ip_to_append)

    out = []
    stack = collections.deque()
    stack.append(IpLevelNode(0, input[0:1], "", input[1:]))
    stack.append(IpLevelNode(0, input[0:2], "", input[2:]))
    stack.append(IpLevelNode(0, input[0:3], "", input[3:]))

    while stack:
        node = stack.popleft()
        curlevel = node.level
        predecessor = node.predecessor
        remaining = node.successor
        if curlevel == 3 and len(remaining) == 0:
            out.append(node.predecessor)
            continue

        i = 1
        while i <= 3:
            if len(remaining) < i:
                break
            ipToAppend = remaining[0:i]
            successor = remaining[i:]
            if len(ipToAppend) > 0:
                numIpToAppend = int(ipToAppend)
            if numIpToAppend <= 255:
                stack.appendleft(IpLevelNode(curlevel + 1, ipToAppend, predecessor, successor))

            i += 1
    return out

print(generate_ip_address(255255255255))