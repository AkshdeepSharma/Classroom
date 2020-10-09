class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = [[0]]
        ans = []
        while paths:
            path = paths.pop()
            for node in graph[path[-1]]:
                if node == len(graph) - 1:
                    ans.append(path + [node])
                else:
                    paths.append(path + [node])
        return ans
