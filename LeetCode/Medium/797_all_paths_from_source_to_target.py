class Solution(object):
    def allPathsSourceTarget(self, graph_list):
        """
        :type graph_list: List[List[int]]
        :rtype: List[List[int]]
        """
        start, end = 0, len(graph_list) - 1
        graph = {}
        res = []
        for i in range(len(graph_list)):
            graph[i] = set()
            for j in range(len(graph_list[i])):
                graph[i].add(graph_list[i][j])

        def dfs(graph, start, end, path=[]):
            path = path + [start]
            if start == end:
                res.append(path)
            for next in graph[start]:
                if next not in path:
                    dfs(graph, next, end, path)
        dfs(graph, start, end)
        return res
