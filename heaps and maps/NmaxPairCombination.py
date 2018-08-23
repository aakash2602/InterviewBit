class MaxHeap():
    def __init__(self):
        self.heap = []
        self.size = 0

    def insert_element(self, value):
        if len(self.heap) <= self.size:
            self.heap.append(value)
        else:
            self.heap[self.size] = value
        self.heapifyUp()
        self.size += 1

    def get_root_element(self):
        value = self.heap[0] if self.size > 0 else None
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return value

    def heapifyUp(self):
        child = self.size
        parent = int((child - 1) / 2)
        while parent != child:
            parent_value = self.heap[parent][0]
            child_value = self.heap[child][0]
            if parent_value >= child_value:
                break
            else:
                self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
                child = parent
                parent = int((child - 1) / 2)

    def heapifyDown(self):
        parent = 0
        while parent <= self.size:
            child = parent
            left_child = parent * 2 + 1
            if left_child < self.size and self.heap[child][0] < self.heap[left_child][0]:
                child = left_child
            right_child = parent * 2 + 2
            if right_child < self.size and self.heap[child][0] < self.heap[right_child][0]:
                child = right_child
            if child == parent:
                break
            self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
            parent = child

    def print_element(self):
        for i in range(self.size):
            print(self.heap[i], end=' ')
        print()


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        A.sort()
        B.sort()
        heap = MaxHeap()
        output = []
        i = 0
        n = len(A)
        index_map = {}
        index_map[n - 1] = {}
        index_map[n - 1][n - 1] = 1
        heap.insert_element((A[n - 1] + B[n - 1], n - 1, n - 1))
        while i < n:
            element = heap.get_root_element()
            print (element)
            output.append(element[0])
            if element[1] - 1 not in index_map:
                print ("inside 1")
                index_map[element[1] - 1] = {}
                index_map[element[1] - 1][element[2]] = 1
                heap.insert_element((A[element[1] - 1] + B[element[2]], element[1] - 1, element[2]))
                print (index_map)
            else:
                if element[2] not in index_map[element[1] - 1]:
                    print("inside 2")
                    index_map[element[1] - 1][element[2]] = 1
                    heap.insert_element((A[element[1] - 1] + B[element[2]], element[1] - 1, element[2]))
                    print(index_map)
                else:
                    print("inside 3")
                    # continue
            if element[1] not in index_map:
                print("inside 4")
                index_map[element[1]] = {}
                index_map[element[1]][element[2] - 1] = 1
                heap.insert_element((A[element[1]] + B[element[2] - 1], element[1], element[2] - 1))
                print(index_map)
            else:
                if element[2] - 1 not in index_map[element[1]]:
                    print("inside 5")
                    index_map[element[1]][element[2] - 1] = 1
                    heap.insert_element((A[element[1]] + B[element[2] - 1], element[1], element[2] - 1))
                    print(index_map)
                else:
                    print("inside 6")
                    # continue
            heap.print_element()
            i += 1
        return output


if __name__ == "__main__":
    sol = Solution()
    print (sol.solve([ 3, 2, 4, 2 ], [ 4, 3, 1, 2 ]))