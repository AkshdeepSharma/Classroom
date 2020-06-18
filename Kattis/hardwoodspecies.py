import sys
from collections import Counter


def main():
    trees = sys.stdin.read().split('\n')
    if trees[-1] == '':
        trees = trees[:-1]
    getTreePercentages(trees)


def getTreePercentages(trees):
    tree_counts = Counter(trees)
    total_trees = len(trees)
    for tree, count in sorted(tree_counts.items()):
        print(f"{tree} {str(round(100 * (count / total_trees), 6))}")


if __name__ == "__main__":
    main()

# I think this problem is impossible to do without Counter. Always times out without it.
