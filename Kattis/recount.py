from collections import defaultdict
votes = defaultdict(int)
name = input()
highest_votes, candidate = 0, []

while name != "***":
    votes[name] += 1
    name = input()

for key, val in votes.items():
    if val == highest_votes:
        candidate.append(key)
    elif val > highest_votes:
        highest_votes = val
        candidate = [key]

if len(candidate) > 1:
    print("Runoff!")
else:
    print(candidate[0])
