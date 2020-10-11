class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj_list = {}
        max_rank = 0
        for i in range(n):
            adj_list[i] = set()
        for x, y in roads:
            adj_list[x].add(y)
            adj_list[y].add(x)
        for i in range(n):
            for j in range(i + 1, n):
                if i in adj_list[j]:
                    max_rank = max(max_rank, len(
                        adj_list[i]) + len(adj_list[j]) - 1)
                else:
                    max_rank = max(max_rank, len(
                        adj_list[i]) + len(adj_list[j]))
        return max_rank
