class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        count = 0
        curr_len, wanted_len = len(arr), len(arr) // 2
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        count_arr = sorted(list(d.values()))
        while True:
            num = count_arr.pop()
            curr_len -= num
            count += 1
            if curr_len <= wanted_len:
                return count
