class Solution():

    def pathSumValues(self, A, B):
        out = []
        self.get_path_sum_values(A, B, 0, [], out)
        return out

    def get_path_sum_values(self, node, sum, current_sum, current_elem, out):
        if node == None:
            return
        current_elem = current_elem[:]
        current_elem.append(node.val)
        current_sum = current_sum + node.val
        if not node.left and not node.right:
            if current_sum == sum:
                out.append(current_elem)
        else:
            self.get_path_sum_values(node.left, sum, current_sum, current_elem, out)
            self.get_path_sum_values(node.right, sum, current_sum, current_elem, out)