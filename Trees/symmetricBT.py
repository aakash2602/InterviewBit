class Solution():

    def symmetricBT(self, A):
        return self.check_symmetry(A.left, A.right)

    def check_symmetry(self, root1, root2):
        if root1 == None and root2 == None:
            return 1
        elif root1 == None or root2 == None:
            return 0
        # elif A.left.val != A.right.val:
        #     return 0
        else:
            if root1.val != root2.val:
                return 0
            val = self.check_symmetry(root1.left, root2.right)
            if val == 0:
                return val
            return self.check_symmetry(root1.right, root2.left)