class Solution():

    def zigZagTree(self, A):
        data = []
        self.get_data(A, data, 0)
        index = 0
        mode = False
        while True:
            # print (mode)
            if index >= len(data):
                break
            if mode:
                # print ("entering")
                data[index] = list(reversed(data[index]))
            index += 1
            mode = False if mode else True
        return data

    def get_data(self, node, data, depth):
        if node == None:
            return
        if depth >= len(data):
            data.append([])
        data[depth].append(node.val)
        self.get_data(node.left, data, depth + 1)
        self.get_data(node.right, data, depth + 1)