class Solution():

    def postorder(self, A):
        out = []
        self.traversal(A, out)
        return out

    def traversal(self, A, out):
        if A == None:
            return
        self.traversal(A.left, out)
        self.traversal(A.right, out)
        out.append(A.val)