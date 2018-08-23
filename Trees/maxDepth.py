class Solution():

    def max_depth(self, head):
        return self.get_depth(head, 0)

    def get_depth(self, head, depth):
        if head == None:
            return depth
        ldepth = self.get_depth(head.left, depth + 1)
        rdepth = self.get_depth(head.right, depth + 1)
        return max(ldepth, rdepth)