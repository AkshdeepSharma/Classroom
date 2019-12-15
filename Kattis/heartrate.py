def calcBPM(beats, seconds):
    return (beats * 60) / seconds


def main():
    N = int(input())
    for _ in range(N):
        beats, seconds = map(float, input().split())
        BPM = calcBPM(beats, seconds)
        min_ABPM = BPM - (60 / seconds)
        max_ABPM = BPM + (60 / seconds)
        print(round(min_ABPM, 4), round(BPM, 4), round(max_ABPM, 4))


if __name__ == '__main__':
    main()
