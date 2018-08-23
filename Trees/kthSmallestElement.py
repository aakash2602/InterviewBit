class Solution():

    def kthSmallestElement(self, A, B):
        index, node = self.get_kth_element(A, B, 0)
        print (node.val)
        print (index)
        return node

    def get_kth_element(self, A, B, index):
        if A == None:
            return index, None
        index, node = self.get_kth_element(A.left, B, index)
        if node != None:
            return index, node
        index += 1
        if index == B:
            return index, A
        return self.get_kth_element(A.right, B, index)