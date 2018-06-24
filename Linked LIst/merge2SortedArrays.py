# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    def merge(self, A, B):
        head = None
        new_list = None
        while A != None and B != None:
            if A.val <= B.val:
                if head == None:
                    head = A
                    new_list = head
                else:
                    new_list.next = A
                    new_list = new_list.next
                A = A.next
            else:
                if head == None:
                    head = B
                    new_list = head
                else:
                    new_list.next = B
                    new_list = new_list.next
                B = B.next
        if A != None:
            if head == None:
                head = A
            else:
                new_list.next = A
        if B != None:
            if head == None:
                head = B
            else:
                new_list.next = B
        return head