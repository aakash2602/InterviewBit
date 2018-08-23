class Node():

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():

    def twoSumBT(self, A, B):
        leftqueue = []
        rightqueue = []

        curr1 = A
        curr2 = A
        val1 = None
        val2 = None
        lflag = True
        rflag = True
        while True:

            while (curr1 != None or leftqueue) and lflag:
                # print (leftqueue)
                if curr1 == None:
                    curr1 = leftqueue.pop()
                    val1 = curr1
                    print (curr1.val)
                    curr1 = curr1.right
                    break
                else:
                    leftqueue.append(curr1)
                    curr1 = curr1.left

            while (curr2 != None or rightqueue) and rflag:
                if curr2 == None:
                    curr2 = rightqueue.pop()
                    val2 = curr2
                    print (curr2.val)
                    curr2 = curr2.left
                    break
                else:
                    rightqueue.append(curr2)
                    curr2 = curr2.right

            if not val1 or not val2:
                return 0
            sum_nums = val1.val + val2.val
            if val1 == val2:
                lflag = True
                rflag = True
                val1 = None
                val2 = None
            elif sum_nums == B:
                return 1
            elif sum_nums > B:
                lflag = False
                rflag = True
                val2 = None
            else:
                lflag = True
                rflag = False
                val1 = None

if __name__ == "__main__":
    sol = Solution()
    head = Node(10)
    node = head
    node.left = Node(5)
    node.right = Node(12)
    left = node.left
    right = node.right
    left.left = Node(4)
    left.right = Node(7)
    left = left.right
    left.right = Node(8)
    right.left = Node(11)
    right.right = Node(17)
    right = right.right
    right.left = Node(16)
    right.right = Node(22)
    print (sol.twoSumBT(head, 44))

    # def get_node(self, node, val):
    #     if node == val:
    #         return node
    #     if node.val > val:
    #         if node.left != None:
    #             return self.get_node(node.left, val)
    #         else:
    #             return node
    #     else:
    #         if node.right != None:
    #             return self.get_node(node.right, val)
    #         else:
    #             return node