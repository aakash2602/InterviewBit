# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        middle = self.get_middle_element(A)
        head_second = self.get_reverse_list(middle)

        output = 1
        ## compare the list
        while A != None and head_second != None:
            if A.val != head_second.val:
                return 0
            A = A.next
            head_second = head_second.next
        return 1

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

if __name__ == "__main__":
    sol = Solution()
    print (sol.lPalin())