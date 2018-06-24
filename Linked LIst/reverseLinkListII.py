# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    def reverseList(self, A, B, C):
        # ptr = A
        if C - B == 0:
            return A
        # for i in range(n-m+1):
        #     ptr = ptr.next
        index = 1
        head = A
        start = None
        end = None
        last = None
        while A != None:
            if index == B - 1:
                start = A
                A = A.next
            elif index >= B and index < C:
                temp = A.next
                A.next = last
                last = A
                A = temp
            elif index == C:
                end = A.next
                A.next = last
                last = A
                break
            else:
                A = A.next
            index += 1
        if start == None:
            head.next = end
            head = last
        else:
            start.next.next = end
            start.next = last
        return head
