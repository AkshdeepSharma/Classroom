def findBestAnimal(valid_animals, animal_letters, letter):
    if not valid_animals:
        return "?"
    for animal in valid_animals:
        if animal[-1] not in animal_letters or (len(animal_letters[animal[-1]]) == 1 and animal_letters[animal[-1]][0] == animal):
            return animal + "!"
    return valid_animals[0]


def main():
    letter = input()[-1]
    animals = [input() for _ in range(int(input()))]
    animal_letters = {}
    valid_animals = []
    for animal in animals:
        if animal[0] not in animal_letters:
            animal_letters[animal[0]] = []
        animal_letters[animal[0]].append(animal)
        if animal[0] == letter:
            valid_animals.append(animal)
    print(findBestAnimal(valid_animals, animal_letters, letter))


if __name__ == "__main__":
    main()
