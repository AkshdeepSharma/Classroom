import heapq

top_bin, bottom_bin = [], []
median = 0
while True:
    try:
        val = input()
        if val == "#":
            if len(bottom_bin) == len(top_bin):
                print(heapq.heappop(top_bin))
            else:
                print(heapq.heappop(bottom_bin) * -1)
        else:
            val = int(val)
            if median == 0:
                heapq.heappush(bottom_bin, val * -1)
                median = val
            elif val > median:
                heapq.heappush(top_bin, val)
                if len(bottom_bin) - len(top_bin) < 0:
                    median = heapq.heappop(top_bin)
                    heapq.heappush(bottom_bin, median * -1)
            else:
                heapq.heappush(bottom_bin, val * -1)
                if len(bottom_bin) - len(top_bin) > 1:
                    median = heapq.heappop(bottom_bin) * -1
                    heapq.heappush(top_bin, median)
    except EOFError:
        break
