def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['F']),
    'F': set(['C', 'E'])
}


def dfs_paths(graph, start, end):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == end:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def number_needed(a, b):
    a, b = list(a), list(b)
    a_vals = list(a)
    for i in a_vals:
        if i in b:
            a.remove(i)
            b.remove(i)
    return len(a) + len(b)


def number_of_deletes(a, b):
    a, b = list(a), list(b)
    values_a = list(a)
    for letter in values_a:
        if letter in b:
            a.remove(letter)
            b.remove(letter)
    return len(a) + len(b)



