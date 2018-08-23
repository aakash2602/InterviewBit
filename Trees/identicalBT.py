class Solution():

    def identicalBT(self, A, B):
        return self.is_identical(A, B)

    def is_identical(self, A, B):
        if A == None and B == None:
            return 1
        elif A == None or B == None:
            return 0
        elif A.val != B.val:
            return 0
        else:
            val = self.is_identical(A.left, B.left)
            if val == 0:
                return 0
            val = self.is_identical(A.right, B.right)
            return val