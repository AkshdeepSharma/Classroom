T = int(input())

for i in range(T):
    image = []
    imageVerticalFlip = []
    mirrorSize = input().split(' ')
    R = int(mirrorSize[0])
    for j in range(R):
        image.append(input()[::-1])

    for k in range(-1, -R - 1, -1):
        imageVerticalFlip.append(image[k])
    print('Test', str(i + 1))
    print("\n".join(imageVerticalFlip))
