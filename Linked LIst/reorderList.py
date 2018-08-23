# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def reorderList(self, A):
        middle = self.get_middle_element(A)
        head_second = self.get_reverse_list(middle)

        if middle == A:
            return A

        head = A
        new_head = head
        A = A.next
        mode = 1
        while A != None or head_second != None:
            if A == head_second:
                head.next = A
                break
            if mode == 1:
                head.next = head_second
                head_second = head_second.next
                mode = 0
            else:
                head.next = A
                A = A.next
                mode = 1
        return new_head

    def get_middle_element(self, head):
        if head == None:
            return head
        fhd = head.next
        while fhd != None:
            head = head.next
            fhd = fhd.next
            fhd = fhd.next if fhd != None else fhd
        return head

    def get_reverse_list(self, head):
        last = None
        while head != None:
            temp = head.next
            head.next = last
            last = head
            head = temp
        return last