import heapq


def get_max_size(num_intersections, corridors):
    dp = [1] + [0] * (num_intersections - 1)
    prev = [None] * num_intersections
    visited = [False] * num_intersections
    heap = []
    heapq.heappush(heap, (-1, 0))
    while heap:
        corridor = heapq.heappop(heap)
        curr_corridor = corridor[1]
        visited[curr_corridor] = True
        corridor_dict = corridors[curr_corridor]
        for connecting_corridors in corridor_dict:
            factor = corridor_dict[connecting_corridors]
            if dp[connecting_corridors] < dp[curr_corridor] * -factor:
                dp[connecting_corridors] = float(dp[curr_corridor] * -factor)
                prev[connecting_corridors] = curr_corridor
                if visited[connecting_corridors] == False:
                    heapq.heappush(
                        heap, (-dp[connecting_corridors], connecting_corridors))
    return dp[-1]


def create_adj_list(num_intersections, num_corridors):
    corridors = {}
    for i in range(num_intersections):
        corridors[i] = {}
    for i in range(num_corridors):
        x, y, f = input().split()
        x, y, f = int(x), int(y), float(f) * -1
        if x == y:
            pass
        elif y in corridors[x] and corridors[x][y] < f:
            pass
        else:
            corridors[x][y], corridors[y][x] = f, f
    return corridors


def main():
    num_intersections, num_corridors = map(int, input().split())
    while num_intersections > 0 and num_corridors > 0:
        corridors = create_adj_list(num_intersections, num_corridors)
        print("{:.4f}".format(abs(get_max_size(num_intersections, corridors))))
        num_intersections, num_corridors = map(int, input().split())


if __name__ == '__main__':
    main()
