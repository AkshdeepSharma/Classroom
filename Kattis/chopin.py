def main():
    try:
        i = 1
        while True:
            note, tonality = input().split()
            keys = {
                'A#': 'Bb',
                'C#': 'Db',
                'D#': 'Eb',
                'F#': 'Gb',
                'G#': 'Ab',
                'Bb': 'A#',
                'Db': 'C#',
                'Eb': 'D#',
                'Gb': 'F#',
                'Ab': 'G#',
            }
            if note not in keys:
                print(f'Case {i}: UNIQUE')
            else:
                print(f'Case {i}: {keys[note]} {tonality}')
            i += 1
    except EOFError:
        pass


if __name__ == "__main__":
    main()
