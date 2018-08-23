class Solution():

    def minDepth(self, A):
        return self.get_depth(A, 1)

    def get_depth(self, head, depth):
        if head == None:
            return 9223372036854775807
        ldepth = self.get_depth(head.left, depth+1)
        rdepth = self.get_depth(head.right, depth+1)
        val = min(ldepth, rdepth)
        if val == 9223372036854775807:
            return depth
        else:
            return val