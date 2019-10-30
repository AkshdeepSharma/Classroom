MOD = 1000000007

N, T = map(int, input().split())
A, B, C, t0 = map(int, input().split())
queue = [t0]
for _ in range(1, N):
    t0 = (((A * t0) + B) % C) + 1
    queue.append(t0)

queue = sorted(queue)

completed_problems, curr_time, penalty_time = 0, 0, 0
while completed_problems < N:
    if curr_time + queue[completed_problems] > T:
        break
    penalty_time = penalty_time + queue[completed_problems] + curr_time
    curr_time += queue[completed_problems]
    completed_problems += 1

print(str(completed_problems), str(penalty_time % MOD))
