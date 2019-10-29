c1 = input().split(' ')
c1 = [int(x) for x in c1]
c2 = input().split(' ')
c2 = [int(x) for x in c2]
c3 = input().split(' ')
c3 = [int(x) for x in c3]
c4 = input().split(' ')
c4 = [int(x) for x in c4]
c5 = input().split(' ')
c5 = [int(x) for x in c5]

sums = [sum(c1), sum(c2), sum(c3), sum(c4), sum(c5)]

print(sums.index(max(sums)) + 1, max(sums))
