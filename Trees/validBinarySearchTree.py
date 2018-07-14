# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isValidBST(self, A):
        if A == None:
            return 1
        return self.checkBST(A, -1, -1)

    def checkBST(self, A, min_val, max_val):
        if A == None:
            return 1
        # print (A.val)
        # print (min_val)
        # print (max_val)
        if A.left != None:
            if A.val < A.left.val:
                return 0
        # print (A.val)
        if A.right != None:
            if A.val > A.right.val:
                return 0
        # print (A.val)
        if A.right != None:
            if A.right.val >= max_val and max_val != -1:
                # print (A.val)
                return 0
        if A.left != None:
            if A.left.val < min_val and min_val != -1:
                # print (A.val)
                return 0
        # print (A.val)
        val1 = self.checkBST(A.left, min_val, max(A.val, min_val))
        if not val1:
            return 0
        min_value = min(A.val + 1, max_val) if max_val != -1 else A.val + 1
        val2 = self.checkBST(A.right, min_value, max_val)
        return val2