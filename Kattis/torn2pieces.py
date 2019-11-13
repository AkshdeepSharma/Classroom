def main():
    N = int(input())
    adjacency_list = {}
    paths = []
    for _ in range(N):
        stations = list(input().split())
        curr_station = stations[0]
        if curr_station not in adjacency_list:
            adjacency_list[curr_station] = set()
        for i in range(1, len(stations)):
            adjacency_list[curr_station].add(stations[i])
            if stations[i] not in adjacency_list:
                adjacency_list[stations[i]] = set()
            adjacency_list[stations[i]].add(curr_station)
    start, end = map(str, input().split())
    if start not in adjacency_list:
        adjacency_list[start] = set()

    def dfs(start, end, graph, path=[]):
        path = path + [start]
        if start == end:
            paths.append(path)
        for next in graph[start]:
            if next not in path:
                dfs(next, end, graph, path)

    dfs(start, end, adjacency_list)
    if paths == []:
        print("no route found")
    else:
        print(" ".join(paths[0]))


if __name__ == '__main__':
    main()
