def bfs(adj_list, curr_file):
    visited, queue, ans = set(), [curr_file], []
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            ans.append(vertex)
            visited.add(vertex)
            if vertex in adj_list:
                queue.extend(adj_list[vertex] - visited)
    return ans


def main():
    rules = int(input())
    adj_list = {}
    for _ in range(rules):
        rule = input().split()
        for i in range(1, len(rule)):
            if rule[i] not in adj_list:
                adj_list[rule[i]] = set()
            adj_list[rule[i]].add(rule[0][:-1])
    changed_file = input()
    ans = bfs(adj_list, changed_file)
    for dep in ans:
        print(dep)


if __name__ == '__main__':
    main()
