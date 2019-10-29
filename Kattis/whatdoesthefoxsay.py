T = int(input())

for i in range(T):
    recording = input().split(' ')
    newSounds, sounds = [], []
    while True:
        animalGoes = input().split(' goes ')
        if animalGoes == ['what does the fox say?']:
            break
        else:
            sounds.append(animalGoes)
    for animalNoise in range(len(sounds)):
        newSounds.append(sounds[animalNoise][1])
    foxSays = [x for x in recording if x not in newSounds]
    print(' '.join(foxSays))
