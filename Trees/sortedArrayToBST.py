class Node():

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():

    def arraytoBalancedBT(self, A):
        head = self.createBBT(A, 0, len(A)-1)
        self.print_tree(head)
        return head

    def createBBT(self, A, min, max):
        if min > max:
            return None
        index = (max + min) // 2
        temp = Node(A[index])
        temp.left = self.createBBT(A, min, index -1)
        temp.right = self.createBBT(A, index + 1, max)
        return temp

    def print_tree(self, head):
        if head == None:
            return
        self.print_tree(head.left)
        print (head.val)
        self.print_tree(head.right)

if __name__ == "__main__":

    sol = Solution()
    print (sol.arraytoBalancedBT([1, 2, 3, 4, 5, 6, 7]))
