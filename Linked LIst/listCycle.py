# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    def listCycle(self, A):
        loop = None
        head = A
        if A == None:
            return loop
        ptr = A.next
        while A != None and ptr != None:
            if A == ptr:
                loop = A
                break
            A = A.next
            ptr = ptr.next.next if ptr.next != None else ptr.next
        if loop == None:
            return loop
        while head != loop:
            head = head.next
            loop = loop.next
        return head