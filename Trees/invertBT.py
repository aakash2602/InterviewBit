class Solution():

    def invertBT(self, A):
        self.invertTree(A)
        return A

    def invertTree(self, head):
        if head == None:
            return
        head.left, head.right = head.right, head.left
        self.invertBT(head.left)
        self.invertBT(head.right)
        return head