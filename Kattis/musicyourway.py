attributes = {}
attributes_list = input().split()
for i, attribute in enumerate(attributes_list):
    attributes[attribute] = i

attributes_list = " ".join(attributes_list)

song_list = []
m = int(input())
for _ in range(m):
    song = input().split()
    song_list.append(song)

n = int(input())
for _ in range(n):
    to_sort_by = attributes[input()]
    song_list = sorted(song_list, key=lambda x: x[to_sort_by])
    print(attributes_list)
    for i in range(len(song_list)):
        print(" ".join(song_list[i]))
    print("")
