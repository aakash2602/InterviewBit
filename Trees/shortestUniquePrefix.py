class Node():

    def __init__(self, x):
        self.val = x
        self.count = 0
        self.nodes = {}

class Solution():

    def shortestUniquePrefix(self, A):
        root = Node('')
        n = len(A)
        for i in range(n):
            self.add_word(root, A[i])
        out = []
        for i in range(n):
            out.append(self.get_prefix(root, A[i]))
        return out

    def add_word(self, root, word):
        letters = [l for l in word]
        head = root
        for letter in letters:
            if letter in head.nodes:
                head = head.nodes[letter]
            else:
                node = Node(letter)
                head.nodes[letter] = node
                head = node
            head.count += 1
        return

    def get_prefix(self, root, word):
        letters = [l for l in word]
        head = root
        prefix = ''
        for letter in letters:
            node = head.nodes[letter]
            prefix += letter
            if node.count == 1:
                return prefix
            else:
                head = head.nodes[letter]
        return prefix

if __name__ == "__main__":
    sol = Solution()
    print (sol.shortestUniquePrefix(["zebra", "dog", "duck", "dove", "zeg"]))