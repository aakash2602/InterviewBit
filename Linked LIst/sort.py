# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    def sort(self, A):
        n = 0
        head = A
        while A != None:
            n += 1
            A = A.next
        A = head
        head = self.mergeSort(A, n)
        return head

    def mergeSort(self, A, n):
        if n == 1:
            return A
        h1 = A
        h2 = A
        index = 0
        while index < n // 2:
            index += 1
            last = h2
            h2 = h2.next
        last.next = None
        h1 = self.mergeSort(h1, n // 2)
        h2 = self.mergeSort(h2, n - (n // 2))

        head = None
        new_head = head
        while h1 != None and h2 != None:
            if h1.val <= h2.val:
                if head == None:
                    head = h1
                    new_head = head
                else:
                    head.next = h1
                    head = head.next
                h1 = h1.next
            else:
                if head == None:
                    head = h2
                    new_head = head
                else:
                    head.next = h2
                    head = head.next
                h2 = h2.next
        if h1 != None:
            head.next = h1
        if h2 != None:
            head.next = h2
        return new_head
