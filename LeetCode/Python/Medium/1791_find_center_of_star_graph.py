class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adjacency_map = {}
        for edge in edges:
            if edge[0] not in adjacency_map:
                adjacency_map[edge[0]] = []
            if edge[1] not in adjacency_map:
                adjacency_map[edge[1]] = []
            adjacency_map[edge[0]].append(edge[1])
            adjacency_map[edge[1]].append(edge[0])
        for key, val in adjacency_map.items():
            if len(val) == len(edges):
                return key
