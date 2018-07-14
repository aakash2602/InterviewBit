class Solution():

    def preorder(self, A):
        out = []
        self.traversal(A, out)
        return out

    def traversal(self, A, out):
        if A == None:
            return
        out.append(A.val)
        self.traversal(A.left, out)
        self.traversal(A.right, out)