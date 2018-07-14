class Solution():

    def flattenBT(self, A):
        return self.get_flatten(A)

    def get_flatten(self, node):
        if node == None:
            return None
        left = self.get_flatten(node.left)
        right = self.get_flatten(node.right)
        node.left = None
        node.right = left
        temp = node
        while temp.right != None:
            temp = temp.right
        temp.right = right
        return node