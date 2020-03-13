def getVillagersWhoKnowEachSong(evenings):
    music = []
    for _ in range(evenings):
        villagers_present = set(list(map(int, input().split()))[1:])
        if 1 in villagers_present:
            music.append(villagers_present)
        else:
            for i in range(len(music)):
                if len(music[i].intersection(villagers_present)) > 0:
                    music[i] = music[i].union(villagers_present)
    return music


def getVillagersWhoKnowAllSongs(music):
    villagers_who_know_all_songs = music[0]
    for i in range(1, len(music)):
        villagers_who_know_all_songs = villagers_who_know_all_songs.intersection(
            music[i])
    return villagers_who_know_all_songs


def main():
    num_villagers = int(input())
    evenings = int(input())
    music = getVillagersWhoKnowEachSong(evenings)
    villagers_who_know_all_songs = getVillagersWhoKnowAllSongs(music)
    for i in range(1, num_villagers + 1):
        if i in villagers_who_know_all_songs:
            print(i)


if __name__ == "__main__":
    main()
