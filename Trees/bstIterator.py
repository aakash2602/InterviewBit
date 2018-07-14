class Node():

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class bstIterator():

    def __init__(self, head):
        self.head = head
        self.queue = []
        self.current_node = self.next_element(self.head)

    def next_element(self, node):
        while node != None or self.queue:
            if node == None:
                temp = self.queue[-1]
                return temp.right
            else:
                self.queue.append(node)
                node = node.left

    def next(self):
        value = self.queue.pop() if self.has_next() else None
        self.current_node = self.next_element(self.current_node)
        if value:
            print (value.val)
        return value

    def has_next(self):
        if self.queue:
            return True
        return False

if __name__ == "__main__":
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
    sol = bstIterator(None)
    index = 0
    while (1):
        sol.next()
        print (sol.has_next())
        index += 1
        if index > 20:
            break