# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    def removeDuplicated(self, A):
        if A == None:
            return
        while A.next != None:
            if A.val == A.next.val:
                A.next = A.next.next
            else:
                A = A.next
        return A
