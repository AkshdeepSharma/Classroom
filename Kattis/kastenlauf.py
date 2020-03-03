def dfs(graph, start, end, visited=None):
    if not visited:
        visited = set()
    if start == end:
        return True
    visited.add(start)
    for next in graph[start] - visited:
        if dfs(graph, next, end, visited):
            return True
    return False


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        graph = {}
        N = int(input())
        start = tuple(map(int, input().split()))
        for _ in range(N):
            store = tuple(map(int, input().split()))
            graph[store] = set()
        end = tuple(map(int, input().split()))
        graph[start] = set()
        graph[end] = set()

        for i in graph:
            for j in graph:
                if i == j or i == end:
                    continue
                dist = distance(i, j) / 50
                if dist <= 20:
                    graph[i].add(j)
        if dfs(graph, start, end):
            print('happy')
        else:
            print('sad')
