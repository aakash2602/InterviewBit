# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    def rotateList(self, A, k):
        ptr = A
        length = 0
        head = A
        while A != None:
            length += 1
            A = A.next
        A = head
        k = k % length
        if k == 0:
            return head
        last = ptr
        for i in range(k+1):
            last = ptr
            ptr = ptr.next
        while ptr != None:
            A = A.next
            last = ptr
            ptr = ptr.next
        new_head = A.next
        A.next = None
        last.next = head
        return new_head