# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    def removeNthNode(self, A, n):
        ptr = A
        for i in range(n+1):
            if ptr != None:
                ptr = ptr.next
            else:
                return A.next
        head = A
        while ptr != None:
            A = A.next
            ptr = ptr.next
        if A.next != None:
            A.next = A.next.next
        return head