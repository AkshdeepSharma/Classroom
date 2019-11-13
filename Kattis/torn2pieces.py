def create_adjacency_list(N):
    adjacency_list = {}
    for _ in range(N):
        stations = list(input().split())
        curr_station = stations[0]
        adjacency_list = add_in_adjacency_list(curr_station, adjacency_list)
        for i in range(1, len(stations)):
            adjacency_list[curr_station].add(stations[i])
            adjacency_list = add_in_adjacency_list(stations[i], adjacency_list)
            adjacency_list[stations[i]].add(curr_station)
    start, end = map(str, input().split())
    adjacency_list = add_in_adjacency_list(start, adjacency_list)
    return adjacency_list, start, end


def add_in_adjacency_list(curr_station, adjacency_list):
    if curr_station not in adjacency_list:
        adjacency_list[curr_station] = set()
    return adjacency_list


def dfs(start, end, graph, path=[]):
    path = path + [start]
    if start == end:
        paths.append(path)
    for next in graph[start]:
        if next not in path:
            dfs(next, end, graph, path)


def main():
    N = int(input())
    adjacency_list, start, end = create_adjacency_list(N)
    dfs(start, end, adjacency_list)
    if paths == []:
        print("no route found")
    else:
        print(" ".join(paths[0]))


if __name__ == '__main__':
    paths = []
    main()
