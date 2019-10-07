try:
    while True:
        dss, dsq, dspq = [], [], []
        q, s, pq = True, True, True
        queries = int(input())
        for _ in range(queries):
            action, element = map(int, input().split())
            if action == 1:
                dss.append(element)
                dspq.append(element)
                dsq.append(element)
            elif action == 2:
                if not s or not dss or element != dss[-1]:
                    s = False
                else:
                    dss.pop()
                if not pq or not dspq or element != max(dspq):
                    pq = False
                else:
                    dspq.pop(dspq.index(max(dspq)))
                if not q or not dsq or element != dsq[0]:
                    q = False
                else:
                    dsq.pop(0)
        if (q and s) or (q and pq) or (s and pq):
            print("not sure")
        elif not q and not pq and not s:
            print("impossible")
        elif q:
            print("queue")
        elif pq:
            print("priority queue")
        else:
            print("stack")
except EOFError:
    pass