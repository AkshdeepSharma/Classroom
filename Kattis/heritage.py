def name_definition(definitions, name, memo={}):
    MOD = 1000000007
    name_definitions = 0
    if name in memo:
        return memo[name]
    if name in definitions:
        name_definitions = definitions[name]
    for i in range(1, len(name)):
        first, second = name[:i], name[i:]
        if first in definitions:
            name_definitions += definitions[first] * \
                name_definition(definitions, second)
    memo[name] = name_definitions % MOD
    return memo[name]


def main():
    num_definitions, name = input().split()
    definitions = {}
    for _ in range(int(num_definitions)):
        word, nums = input().split()
        definitions[word] = int(nums)
    name_definitions = name_definition(definitions, name)
    print(name_definitions)


if __name__ == "__main__":
    main()
