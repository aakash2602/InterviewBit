import heapq

class Heap():
    def __init__(self):
        self.A = []
        self.length = 0

    def insert(self, val):
        self.A.append(val)
        self.heapifyUp()
        self.length += 1

    def get_max(self):
        if self.length <= 0:
            return None
        value = self.A[0]
        if self.length > 1:
            self.A[0] = self.A.pop(self.length - 1)
        else:
            self.A = []
        self.length -= 1
        self.heapifyDown()
        return value

    def heapifyUp(self):
        child = self.length
        parent = (child - 1) // 2
        while child > 0:
            parent_value = self.A[parent]
            child_value = self.A[child]
            if parent_value >= child_value:
                break
            else:
                self.A[parent], self.A[child] = self.A[child], self.A[parent]
                child = parent
                parent = (child - 1) // 2
                # print (f"{child}::{parent}")

    def heapifyDown(self):
        index = 0
        while index < self.length:
            c1 = 2 * index + 1
            c2 = 2 * index + 2
            child = index
            if c1 < self.length and self.A[c1] > self.A[child]:
                child = c1

            if c2 < self.length and self.A[c2] > self.A[child]:
                child = c2

            if child == index:
                break

            self.A[child], self.A[index] = self.A[index], self.A[child]
            index = child

    def print_element(self):
        for i in range(self.length):
            print (self.A[i], end=' ')

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def magicianChocolates(self, A, B):
        heap = Heap()
        for i in range(len(B)):
            heap.insert(B[i])
            print(heap.print_element())
        print (heap.print_element())
        out = 0
        div = pow(10, 9) + 7
        for i in range(A):
            val = heap.get_max()
            print (val)
            if not val:
                break
            out = (out + (val % div)) % div
            heap.insert(val // 2)
            print(heap.print_element())
        return out

    def nchoc(self, A, B):
        heap = []
        for i in range(len(B)):
            heapq.heappush(heap, -B[i])
        # print (heap)
        out = 0
        div = pow(10, 9) + 7
        for i in range(A):
            val = heapq.heappop(heap) if B else None
            print (val)
            if not val:
                break
            out = (out + (-val % div)) % div
            heapq.heappush(heap, -(-val // 2))
            print(heap)
        return out

if __name__ == "__main__":
    sol = Solution()
    # print(sol.magicianChocolates(11,
    #                 [18, 90, 18, 15, 94, 60, 45, 39, 38, 77, 56, 70, 67, 91, 85, 90, 44, 26, 40, 10, 63, 36, 60, 10, 30,
    #                  47, 76, 11, 69, 38, 51, 38, 79, 68, 5, 72, 80, 49, 63]))
    print (sol.nchoc(11, [18, 90, 18, 15, 94, 60, 45, 39, 38, 77, 56, 70, 67, 91, 85, 90, 44, 26, 40, 10, 63, 36, 60, 10, 30,
                     47, 76, 11, 69, 38, 51, 38, 79, 68, 5, 72, 80, 49, 63]))
    # sol = Heap()
    # print (sol.get_max())
    # sol.insert(10)
    # sol.printHeap()
    # sol.insert(20)
    # sol.printHeap()
    # sol.insert(3)
    # sol.printHeap()
    # sol.insert(4)
    # sol.printHeap()
    # print (sol.get_max())
    # sol.printHeap()
