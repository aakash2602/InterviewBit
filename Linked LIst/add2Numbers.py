# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    def add2Numbers(self, A, B):
        carry = 0
        head = None
        new_head = None
        while A != None or B != None:
            val1 = 0 if A == None else A.val
            val2 = 0 if B == None else B.val
            sum = val1 + val2 + carry
            carry = sum // 10
            if head == None:
                head = ListNode(sum%10)
                new_head = head
            else:
                temp = ListNode(sum%10)
                head.next = temp
                head = head.next
            A = A.next if A != None else A
            B = B.next if B != None else B
        if carry != 0:
            temp = ListNode(carry)
            head.next = temp
            head = head.next
        return new_head
