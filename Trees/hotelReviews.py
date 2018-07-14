class Node:

    def __init__(self, word):
        self.val = word
        self.left = None
        self.right = None

class Solution():

    def hotelReviews(self, A, B):
        words = A.strip().split('_')
        words.sort()
        head = self.createTrie(words, 0, len(words)-1)
        self.print_tree(head)
        n = len(B)
        out = []
        for i in range(n):
            review_words = B[i].split('_')
            goodness_score = self.get_goodness(head, review_words)
            # print (f"{review_words}:{goodness_score}")
            out.append((goodness_score, i))
        out.sort(key= lambda x: x[0], reverse=True)
        new_out = []
        for i in range(n):
            new_out.append(out[i][1])
        return new_out

    def createTrie(self, words, min, max):
        if min > max:
            return None
        index = (max + min) // 2
        temp = Node(words[index])
        temp.left = self.createTrie(words, min, index -1)
        temp.right = self.createTrie(words, index + 1, max)
        return temp

    def get_goodness(self, head, words):
        score = 0
        n = len(words)
        for i in range(n):
            score += self.check_word(head, words[i])
            # print (f"{words[i]}::{score}")
        return score

    def check_word(self, head, word):
        if head == None:
            return 0
        if head.val == word:
            return 1
        if head.val > word:
            return self.check_word(head.left, word)
        else:
            return self.check_word(head.right, word)

    def print_tree(self, head):
        if head == None:
            return
        self.print_tree(head.left)
        print (head.val)
        self.print_tree(head.right)

if __name__ == "__main__":
    sol = Solution()
    print (sol.hotelReviews("cold ", [ "cold_x_X_X_X", "cold_C_C_C_C", "cold_c_C_C_C" ]))