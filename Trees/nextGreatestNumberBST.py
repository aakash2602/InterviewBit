# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        value = None
        # print (A.val)
        # print (B)
        while A != None:
            if A.val > B:
                if not value or A.val < value.val:
                    value = A
                A = A.left
            elif A.val <= B:
                A = A.right
        return value