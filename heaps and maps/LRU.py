import heapq

class Node():

    def __init__(self, key, value):
        self.next = None
        self.prev = None
        self.value = value
        self.key = key

class Solution():

## Best Solution is with double link list and Map

    def lru(self, A):
        self.size = 0
        self.max_size = A
        self.head = None
        self.tail = None
        # self.heap = []
        self.hash_map = {}

    def get(self, key):
        if key not in self.hash_map or self.hash_map[key] == -1:
            return -1
        key_value = self.hash_map[key]
        if key_value == self.head:
            return key_value.value
        if key_value == self.tail:
            self.tail = key_value.prev

        if key_value.prev != None:
            key_value.prev.next = key_value.next
        if key_value.next != None:
            key_value.next.prev = key_value.prev
        key_value.prev = None
        key_value.next = self.head
        self.head.prev = key_value
        self.head = key_value
        if self.tail == None:
            self.tail = key_value
        return key_value.value

        # if key not in self.hash_map or self.hash_map[key][1] == -1:
        #     return -1
        # key_value = self.hash_map[key]
        # index = self.heap.index((key_value[0], key))
        # self.heap[index] = (self.number, key)
        # self.hash_map[key] = (self.number, key_value[1])
        # self.number += 1
        # heapq.heapify(self.heap)
        # return self.hash_map[key][1]

    def set(self, key, value):
        if key not in self.hash_map:
            if self.size < self.max_size:
                new_node = Node(key, value)
                new_node.next = self.head
                if self.head != None:
                    self.head.prev = new_node
                    self.hash_map[self.head.key] = self.head
                self.head = new_node
                self.hash_map[key] = new_node
                self.size += 1
                if self.tail == None:
                    self.tail = new_node
            else:
                temp = self.tail
                self.tail = self.tail.prev
                if self.tail != None:
                    self.tail.next = None
                new_node = Node(key, value)
                if temp != self.head:
                    new_node.next = self.head
                    self.head.prev = new_node
                self.head = new_node
                self.hash_map[key] = new_node
                self.hash_map[temp.key] = -1
                if self.tail == None:
                    self.tail = new_node
                del (temp)
        else:
            key_value = self.hash_map[key]
            if key_value == -1:
                temp = self.tail
                self.tail = self.tail.prev
                if self.tail != None:
                    self.tail.next = None
                self.hash_map[temp.key] = -1
                new_node = Node(key, value)
                if temp != self.head:
                    new_node.next = self.head
                    self.head.prev = new_node
                self.head = new_node
                self.hash_map[key] = new_node
                if self.tail == None:
                    self.tail = new_node
                del (temp)
            else:
                if key_value == self.head:
                    key_value.value = value
                    return
                if key_value == self.tail:
                    self.tail = key_value.prev
                if key_value.prev != None:
                    key_value.prev.next = key_value.next
                if key_value.next != None:
                    key_value.next.prev = key_value.prev
                key_value.prev = None
                key_value.next = self.head
                self.head.prev = key_value
                self.head = key_value
                self.head.value = value
                self.hash_map[key] = key_value
                if self.tail == None:
                    self.tail = key_value

        # if key not in self.hash_map:
        #     if self.size < self.max_size:
        #         heapq.heappush(self.heap, (self.number, key))
        #         self.hash_map[key] = (self.number, value)
        #         self.number += 1
        #         self.size += 1
        #     else:
        #         val = heapq.heappop(self.heap)
        #         self.hash_map[val[1]] = (-1, -1)
        #         heapq.heappush(self.heap, (self.number, key))
        #         self.hash_map[key] = (self.number, value)
        #         self.number += 1
        # else:
        #     key_value = self.hash_map[key]
        #     if key_value[1] == -1:
        #         val = heapq.heappop(self.heap)
        #         self.hash_map[val[1]] = (-1, -1)
        #         heapq.heappush(self.heap, (self.number, key))
        #         self.hash_map[key] = (self.number, value)
        #         self.number += 1
        #     else:
        #         index = self.heap.index((key_value[0], key))
        #         self.heap[index] = (self.number, key)
        #         heapq.heapify(self.heap)
        #         self.hash_map[key] = (self.number, value)
        #         self.number += 1

    def print_element(self):
        # print (self.head)
        # print(self.head.prev)
        # print(self.head.next)
        # print(self.tail)
        # print(self.tail.prev)
        # print(self.tail.next)
        temp = self.head
        index = 0
        print (f"head : {self.head} :::: tail : {self.tail}")
        while temp != None:
            print (f"link list values::{temp}::{temp.next}::{temp.prev}")
            temp = temp.next
            index += 1
            if index > 10:
                break
        print (self.hash_map)

if __name__ == "__main__":
    sol = Solution()
    # sol.lru(4)
    # sol.set(5, 13)
    # sol.set(9, 6)
    # sol.set(4, 1)
    # sol.print_element()
    # print (sol.get(4))
    # sol.print_element()
    # sol.set(6, 1)
    # sol.print_element()
    # sol.set(8, 11)
    # sol.print_element()
    # print (sol.get(13))
    # print(sol.get(1))
    # sol.set(8, 11)
    # sol.print_element()
    # sol.set(12, 12)
    # sol.print_element()
    # print(sol.get(10))
    # sol.set(15, 13)
    # sol.print_element()
    # sol.set(2, 13)
    # sol.print_element()
    # sol.set(7, 5)
    # sol.print_element()
    # sol.set(10, 3)
    # sol.print_element()
    # print(sol.get(6))
    # print(sol.get(10))
    # sol.set(15, 14)
    # sol.set(5, 12)
    # sol.print_element()
    # print(sol.get(5))
    # print(sol.get(7))
    # print(sol.get(15))
    # print(sol.get(5))
    # print(sol.get(6))
    # print(sol.get(10))
    # sol.set(7, 13)
    # print(sol.get(14))
    # sol.set(8, 9)
    # print(sol.get(4))
    # sol.set(6, 11)
    # print(sol.get(9))
    # sol.set(6, 12)
    # print(sol.get(3))
    # sol.print_element()
    ## 32 4 S 5 13 S 9 6 S 4 1 G 4 S 6 1 S 8 11 G 13 G 1 S 12 12 G 10 S 15 13 S 2 13 S 7 5 S 10 3 G 6 G 10 S 15 14 S 5 12 G 5 G 7 G 15 G 5 G 6
    # G 10 S 7 13 G 14 S 8 9 G 4 S 6 11 G 9 S 6 12 G 3

    sol.lru(1)
    sol.set(2, 1)
    sol.print_element()
    sol.set(2, 2)
    sol.print_element()
    print (sol.get(2))
    sol.set(1, 1)
    sol.print_element()
    sol.set(4, 1)
    sol.print_element()
    print(sol.get(2))

    # print(sol.get(1))
    # sol.set(1, 10)
    # sol.set(5, 12)
    # sol.print_element()
    # sol.set(1, 12)
    # sol.print_element()
    # sol.set(6, 14)
    # sol.print_element()
    # print (sol.get(5))
    # print (sol.get(1))
    # print (sol.get(6))
    # print (sol.get(1))
    # sol.set(5, 15)
    # sol.print_element()