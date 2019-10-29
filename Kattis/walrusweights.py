N = int(input())
weights = []
for i in range(N):
    weights.append(int(int(input())))

if all(w > 1000 for w in weights):
    print(min(weights))
    quit()

