class Solution():

    def inorder(self, A):
        out = []
        self.traversal(A, out)
        return out

    def traversal(self, A, out):
        if A == None:
            return
        self.traversal(A.left, out)
        out.append(A.val)
        self.traversal(A.right, out)