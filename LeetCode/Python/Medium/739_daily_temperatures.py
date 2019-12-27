def daily_temp(self, T):
    ans = [0] * len(T)
    stack = []
    for i, t in enumerate(T):
        while stack and t[stack[-1]] < t:
            cur = stack.pop()
            ans[cur] = i - cur
        stack.append(i)
    return ans
