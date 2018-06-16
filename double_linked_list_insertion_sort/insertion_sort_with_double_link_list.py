class Node:
    def __init__(self, num):
        self.next = None
        self.prev = None
        self.number = num

    def add_next(self, node):
        self.next = node

    def add_prev(self, node):
        self.prev = node


t = int(input().strip())
for test_cases in range(t):
    n = int(input().strip())
    inp_array = input().strip().split()
    inp_array = [int(elem) for elem in inp_array]

    root = Node(inp_array[0])
    last = root
    total_count = 0
    for i in range(1, n):
        count = 0
        new_node = Node(inp_array[i])
        # print (last.number)
        # print(new_node.number)
        if last.number <= new_node.number:
            last.next = new_node
            new_node.prev = last
            last = new_node
        else:
            count = 1
            previous_node = last
            mode = 0
            while previous_node.prev != None:
                # print (previous_node.prev.number)
                if previous_node.prev.number <= new_node.number:
                    new_node.next = previous_node
                    new_node.prev = previous_node.prev
                    previous_node.prev.next = new_node
                    previous_node.prev = new_node
                    # print (previous_node.prev.number)
                    # print(previous_node.prev.next.number)
                    mode = 1
                    break
                count = count + 1
                previous_node = previous_node.prev
            if mode == 0:
                # print(previous_node.number)
                new_node.next = previous_node
                previous_node.prev = new_node
                #        for j in range(i - 1, -1, -1):
                #            if inp_array[j] > inp_array[i]:
                #                count = count + 1
        # print (count)
        total_count = total_count + count
    print(total_count)