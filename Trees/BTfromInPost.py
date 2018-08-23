class Node():

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():

    def BTfromInPost(self, A, B):
        head = self.get_BT(A, B)
        return head

    def get_BT(self, A, B):
        if not A:
            return None
        n = len(B)
        node = Node(B[n-1])
        index = A.index(B[n-1])
        node.left = self.get_BT(A[:index], B[:index])
        node.right = self.get_BT(A[index+1:], B[index:n-1])
        return node

    def print_inorder(self, node):
        if node == None:
            return
        self.print_inorder(node.left)
        print (node.val)
        self.print_inorder(node.right)

if __name__ == "__main__":

    sol = Solution()
    head = sol.BTfromInPost([4, 8, 2, 5, 1, 6, 3, 7], [8, 4, 5, 2, 6, 7, 3, 1])
    sol.print_inorder(head)