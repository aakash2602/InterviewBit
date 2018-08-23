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
        last = None
        mode = 0
        head = A
        while A.next != None:
            if A.val == A.next.val:
                A.next = A.next.next
                mode = 1
            else:
                if mode == 1:
                    if last == None:
                        head = A.next
                        A = A.next
                    else:
                        last.next = A.next
                        A = A.next
                    mode = 0
                else:
                    last = A
                    A = A.next
        if mode == 1:
            if last == None:
                head = A.next
            else:
                last.next = A.next
        return head
