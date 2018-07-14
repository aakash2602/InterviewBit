class Node():

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():

    def revoverBST(self, A):
        first = []
        middle = []
        last = []
        last_value = []
        self.get_abnormal_nodes(A, first, middle, last, last_value)
        if last:
            return [first[0].val, last[0].val]
        else:
            return [first[0].val, middle[0].val]
        # for node in nodes:
        #     print (node.val)
        # if len(nodes) == 2:
        #     return [nodes[0].val, nodes[1].val]
        # else:
        #     node = nodes[0]
        #     if node.left:
        #         if node.val < node.left.val:
        #             return [node.val, node.left.val]
        #     if node.right:
        #         if node.val > node.right.val:
        #             return [node.val, node.right.val]

    def get_abnormal_nodes(self, node, first, middle, last, last_value):
        if node == None:
            return
        self.get_abnormal_nodes(node.left, first, middle, last, last_value)
        if last_value:
            if node.val < last_value[0].val:
                # print (node.val)
                if first:
                    last.append(node)
                else:
                    first.extend(last_value)
                    middle.append(node)
        if last_value:
            last_value[0] = node
        else:
            last_value.append(node)
        self.get_abnormal_nodes(node.right, first, middle, last, last_value)
    # def get_abnormal_nodes(self, node, nodes):
    #     if node == None:
    #         return
    #     if node.left and node.right:
    #         if node.left.val > node.val and node.val < node.right.val:
    #             if node.left not in nodes:
    #                 print(1)
    #                 print (node.left.val)
    #                 nodes.append(node.left)
    #         elif node.left.val > node.val and node.val > node.right.val:
    #
    #         if node.right.val < node.val:
    #             if node not in nodes:
    #                 print (4)
    #                 print (node.val)
    #                 nodes.append(node)
    #     elif node.left:
    #         if node.val < node.left.val:
    #             if node.left not in nodes:
    #                 print(2)
    #                 print(node.left.val)
    #                 nodes.append(node.left)
    #     elif node.right:
    #         if node.val > node.right.val:
    #             if node not in nodes:
    #                 print(3)
    #                 print(node.val)
    #                 nodes.append(node)
    #     self.get_abnormal_nodes(node.left, nodes)
    #     self.get_abnormal_nodes(node.right, nodes)

if __name__ == "__main__":
    head = Node(100)
    node = head
    node.left = Node(50)
    node.right = Node(108)
    left = node.left
    right = node.right
    left.left = Node(25)
    left.right = Node(75)
    left = left.right
    left.right = Node(85)
    right.left = Node(101)
    right.right = Node(116)
    right = right.right
    right.left = Node(120)
    right.right = Node(124)
    sol = Solution()
    print (sol.revoverBST(head))