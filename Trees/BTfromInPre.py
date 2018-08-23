class Node():

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():

    def BTfromInPre(self, A, B):
        head = self.get_BT(A, B)
        return head

    def get_BT(self, A, B):
        if not A:
            return None
        node = Node(A[0])
        index = B.index(A[0])
        node.left = self.get_BT(A[1:index+1], B[:index])
        node.right = self.get_BT(A[index+1:], B[index+1:])
        return node

    def print_inorder(self, node):
        if node == None:
            return
        self.print_inorder(node.left)
        self.print_inorder(node.right)

if __name__ == "__main__":

    sol = Solution()
    head = sol.BTfromInPre([ 1, 2, 3, 4, 5 ], [ 3, 2, 4, 1, 5 ])
    sol.print_inorder(head)