class Solution():

    def balancedBT(self, A):
        height_diff = self.check_height(A)
        if height_diff == -1:
            return 0
        else:
            return 1

    def check_height(self, A):
        if A == None:
            return 0
        left_height = self.check_height(A.left)
        if left_height == -1:
            return -1
        right_height = self.check_height(A.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1