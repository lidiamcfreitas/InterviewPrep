num_test_cases = int(input())


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.children = []


class Trie(TreeNode):
    def __init__(self, x, level):
        super(Trie, self).__init__(x)
        self.level = level

    def add_word(self, word):

        if len(word) == 0:
            return

        first_letter = word[0]

        for child in self.children:
            if child.value == first_letter:
                child.add_word(word[1:])
                return

        new_trie = Trie(first_letter, self.level+1)
        new_trie.add_word(word[1:])
        self.children.append(new_trie)


def main():
    results = []

    for i in range(num_test_cases):
        n, l = [int(_) for _ in input().strip().split()]
        words = set()

        for i in range(n):
            words.add(input().strip())

        results.append(iteration(l, words))

    for i, result in enumerate(results, 1):
        print("Case #{}: {}".format(i, result))


def iteration(l, words):
    sets = [set() for _ in range(l)]

    for word in words:
        for j in range(l):
            sets[j].add(word[j])

    if l == 1:
        return '-'

    elif l == 2:
        for i in sets[0]:
            for j in sets[1]:
                if i + j not in words:
                    return i + j
    # else:
    #     root = Trie('start', 0)
    #     for word in words:
    #         root.add_word(word)
    #
    #     level = 0
    #
    #     to_check = []
    #
    #     to_check.append(root)
    #     while to_check:
    #         current = to_check.pop()
    #         level_chars = sets[current.level]
    #
    #         if len(current.children) != len(level_chars):
    #             # found!
    #             pass
    #         else:
    #             pass
    #
    return '-'


main()

'''
5
4 1
A
B
C
D
4 2
WW
AA
SS
DD
4 2
AA
AB
BA
BB
3 4
CAKE
TORN
SHOW
5 7
HELPIAM
TRAPPED
INSIDEA
CODEJAM
FACTORY
'''

'''
Case #1: -
Case #2: WA
Case #3: -
Case #4: CORN
Case #5: HOLIDAY
'''