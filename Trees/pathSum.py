class Solution():

    def path(self, A, B):
        return self.check_path_sum(A, B, 0)

    def check_path_sum(self, node, sum, current_sum):
        if node == None:
            return 0
        if not node.left and not node.right:
            new_sum = current_sum + node.val
            if new_sum == sum:
                return 1
            return 0
        lcheck = self.check_path_sum(node.left, sum, current_sum + node.val)
        rcheck = self.check_path_sum(node.right, sum, current_sum + node.val)
        return max(lcheck, rcheck)