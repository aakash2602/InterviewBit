# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        if A == None:
            return []
        hash_map = {}
        min_width = self.recurNode(A, hash_map, 0, 0)
        # print (hash_map)
        # print (min_width)
        out = []
        while min_width in hash_map:
            hash_map[min_width].sort(key=lambda x: x[0])
            vertical = []
            for i in range(len(hash_map[min_width])):
                vertical.append(hash_map[min_width][i][1])
            out.append(vertical)
            min_width += 1
        return out

    def recurNode(self, node, hash_map, depth, width):
        if node == None:
            return width + 1
        if width not in hash_map:
            hash_map[width] = [(depth, node.val)]
        else:
            hash_map[width].append((depth, node.val))
        new_width = self.recurNode(node.left, hash_map, depth + 1, width - 1)
        # print (node.val)
        # print (new_width)
        new_width1 = self.recurNode(node.right, hash_map, depth + 1, width + 1)
        return min(new_width, new_width1)

if __name__ == "__main__":
    sol = Solution()
    # print (sol.verticalOrderTraversal(root))

