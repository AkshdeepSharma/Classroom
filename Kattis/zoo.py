def getAnimalCount(animals, test_case):
    d = {}
    res = []
    for animal in animals:
        animal_type = animal.split()[-1]
        if animal_type in d:
            d[animal_type] += 1
        else:
            d[animal_type] = 1
    for key, val in d.items():
        res.append(key + " | " + str(val))
    res = ["List " + str(test_case) + ":"] + sorted(res)
    return res


def main():
    num_animals = int(input())
    test_case = 0
    while num_animals != 0:
        animals = []
        test_case += 1
        for _ in range(num_animals):
            animals.append(input().lower())
        animal_count = getAnimalCount(animals, test_case)
        for animal in animal_count:
            print(animal)
        num_animals = int(input())


if __name__ == "__main__":
    main()
