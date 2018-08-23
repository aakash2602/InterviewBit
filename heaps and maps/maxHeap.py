class MaxHeap():

    def __init__(self):
        self.heap = []
        self.size = 0

    def insert_element(self, value):
        self.heap.append(value)
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
        parent = int((child - 1)/2)
        while parent != child:
            parent_value = self.heap[parent]
            child_value = self.heap[child]
            if parent_value >= child_value:
                break
            else:
                self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
                child = parent
                parent = int((child - 1)/2)

    def heapifyDown(self):
        parent = 0
        while parent <= self.size:
            child = parent
            left_child = parent * 2 + 1
            if left_child < self.size and self.heap[child] < self.heap[left_child]:
                    child = left_child
            right_child = parent * 2 + 2
            if right_child < self.size and self.heap[child] < self.heap[right_child]:
                    child = right_child
            if child == parent:
                break
            self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
            parent = child

    def print_element(self):
        for i in range(self.size):
            print (self.heap[i], end=' ')
        print ()

if __name__ == "__main__":
    heap = MaxHeap()
    heap.insert_element(15)
    heap.print_element()
    heap.insert_element(15)
    heap.print_element()
    heap.insert_element(15)
    heap.print_element()
    heap.insert_element(15)
    heap.print_element()
    heap.insert_element(7)
    heap.print_element()
    heap.insert_element(7)
    heap.print_element()
    print (heap.get_root_element())
    print(heap.get_root_element())
    print(heap.get_root_element())
    print(heap.get_root_element())
    heap.print_element()
