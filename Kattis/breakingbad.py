class Node:
    def __init__(self, name):
        self.name = name
        self.connected = []
        self.colour = None


def split_items(item_list, nodes):
    walter_items, jesse_items = [], []
    stack = []
    visited = set()
    for item in item_list:
        if item in visited:
            continue
        nodes[item].colour = True
        stack.append(nodes[item])
        while stack:
            curr_item = stack.pop()
            if curr_item.name in visited:
                continue
            visited.add(curr_item.name)
            if curr_item.colour:
                walter_items.append(curr_item.name)
            else:
                jesse_items.append(curr_item.name)
            for connected_item in curr_item.connected:
                if connected_item.colour is None:
                    connected_item.colour = not curr_item.colour
                    stack.append(connected_item)
                elif connected_item.colour == curr_item.colour:
                    return "impossible"
    print(" ".join(walter_items))
    return " ".join(jesse_items)


def update_connections(nodes):
    num_connections = int(input())
    for _ in range(num_connections):
        item1, item2 = input().split()
        nodes[item1].connected.append(nodes[item2])
        nodes[item2].connected.append(nodes[item1])
    return nodes


def main():
    num_items = int(input())
    item_list = [input() for _ in range(num_items)]
    nodes = {name: Node(name) for name in item_list}
    update_connections(nodes)
    print(split_items(item_list, nodes))


if __name__ == "__main__":
    main()
