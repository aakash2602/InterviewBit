import collections
import time

class Node:
    def __init__(self):
        self.left_child = None  # corresponds to bit 0
        self.right_child = None  # corresponds to bit 1
        self.terminus = False
        self.bit_index = []
        self.word = ""

    def add(self, child_node, bit, bit_index):
        if bit == '0':
            self.left_child = child_node
            self.left_child.bit_index.append(bit_index)
        elif bit == '1':
            self.right_child = child_node
            self.right_child.bit_index.append(bit_index)

    def update_terminus(self, status):
        self.terminus = status

    def print_node(self):
        print(self.bit_index)
        print(self.terminus)
        print(self.left_child)
        print(self.right_child)
        print(self.word)

class Trie:
    def __init__(self):
        self.head = Node()
        # print (self.head.bit_index)
        # print ("head created")

    def insert(self, num, index):
        word = '{0:016b}'.format(num)
        root = self.head
        for i in range(len(word)):
            # print (root.bit_index)
            # print (i)
            if self.has_node(root, word[i]):
                root = root.left_child if word[i] == '0' else root.right_child
                root.bit_index.append(index)
            else:
                child_node = Node()
                root.add(child_node, word[i], index)
                # root.print_node()
                root = root.left_child if word[i] == '0' else root.right_child
                # root.print_node()

            if i == len(word) - 1:
                # print (" inside terminus array")
                root.update_terminus(True)
                root.word = word
                # root.print_node()

    def has_node(self, node, bit):
        if node == None:
            return False
        if bit == '0':
            return True if node.left_child != None else False
        elif bit == '1':
            return True if node.right_child != None else False

    def print(self):
        root = self.head
        queue = collections.deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            print(node.bit_index)
            if node.terminus == True:
                print("word is: " + node.word)
            if node.left_child != None:
                queue.append(node.left_child)
            if node.right_child != None:
                queue.append(node.right_child)

    def find_max_xor_old(self, num):
        word = '{0:016b}'.format(num)
        root = self.head
        optimal_num = -1
        for i in range(len(word)):
            if word[i] == '0':
                root = root.right_child if root.right_child != None else root.left_child
            elif word[i] == '1':
                root = root.left_child if root.left_child != None else root.right_child

            if root.terminus == True:
                optimal_num = int(root.word, 2)
                break

        return optimal_num

    def find_max_xor(self, num, start, end):
        word = '{0:016b}'.format(num)
        root = self.head
        optimal_num = -1
        for i in range(len(word)):
            # print (i)
            if word[i] == '0':
                if root.right_child != None:
                    mode = 0
                    for k in range(start, end):
                        if k in root.right_child.bit_index:
                            root = root.right_child
                            mode = 1
                            break
                    if mode == 0:
                        root = root.left_child
                else:
                    root = root.left_child
                # root = root.right_child if root.right_child != None else root.left_child
            elif word[i] == '1':
                if root.left_child != None:
                    mode = 0
                    for k in range(start, end):
                        if k in root.left_child.bit_index:
                            root = root.left_child
                            mode = 1
                            break
                    if mode == 0:
                        root = root.right_child
                else:
                    root = root.right_child
                # root = root.left_child if root.left_child != None else root.right_child

            if root.terminus == True:
                optimal_num = int(root.word, 2)
                break

        return optimal_num


millis=int(round(time.time()*1000))
t = int(input().strip())
for test_cases in range(t):
    n, m = input().strip().split(" ")
    n, m = [int(n), int(m)]
    nums = input().strip().split(" ")
    nums = [int(num) for num in nums]
    t = Trie()
    # insert_arr = list(set(nums[x - 1:y]))
    for j in range(len(nums)):
        t.insert(nums[j], j)
    # t.print()
    for i in range(m):
        a, x, y = input().strip().split()
        a, x, y = [int(a), int(x), int(y)]
        max_num = t.find_max_xor(a, x-1, y)
        # print (max_num)
        # t = Trie()
        # nums_new = nums[x-1:y]
        # for j in range(len(nums_new)):
        #     t.insert(nums[j], j)
        # max_num = t.find_max_xor_old(a)
        print(a ^ max_num)
millis1=int(round(time.time()*1000))
print("timetakenforinternalparse:"+str(millis1-millis)+"ms")