def getProblemCategories(categories, words_associated_with_category, problem_statement):
    category_count = {}
    answer = []
    for category in categories:
        category_count[category] = 0
        for word in words_associated_with_category[category]:
            category_count[category] += problem_statement.count(word)
    highest_score = max(category_count.values())
    for category in category_count:
        if category_count[category] == highest_score:
            answer.append(category)
    return sorted(answer)


def main():
    number_of_categories = int(input())
    categories = []
    words_associated_with_category = {}
    problem_statement = []
    for _ in range(number_of_categories):
        inp = input().split()
        categories.append(inp[0])
        words_associated_with_category[inp[0]] = inp[2:]
    try:
        while True:
            problem_statement.extend(input().split())
    except EOFError:
        pass
    answer = getProblemCategories(
        categories, words_associated_with_category, problem_statement)
    for category in answer:
        print(category)


if __name__ == "__main__":
    main()
