class ListNode():
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution():

    def mergeKLists(self, A):

        def merge2lists(l1, l2):
            dummy = ListNode(0)
            current = dummy
            while l1 or l2:
                if not l1:
                    current.next = l2
                    l2 = l2.next
                elif not l2:
                    current.next = l1
                    l1 = l1.next
                elif l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            return dummy.next

        if not A:
            return None
        left = 0
        right = len(A) - 1
        while right > 0:
            if left >= right:
                left = 0
            A[left] = merge2lists(A[left], A[right])
            left += 1
            right -= 1
        return A[0]


    # def mergeKLists(self):
    #     def mergeTwoLists(l1, l2):
    #         curr = dummy = ListNode(0)
    #         while l1 and l2:
    #             if l1.val < l2.val:
    #                 curr.next = l1
    #                 l1 = l1.next
    #             else:
    #                 curr.next = l2
    #                 l2 = l2.next
    #             curr = curr.next
    #         curr.next = l1 or l2
    #         return dummy.next
    #
    #     if not A:
    #         return None
    #     left, right = 0, len(A) - 1;
    #     while right > 0:
    #         if left >= right:
    #             left = 0
    #         else:
    #             A[left] = mergeTwoLists(A[left], A[right])
    #             left += 1
    #             right -= 1
    #     return A[0]

if __name__  == "__main__":
    sol = Solution
    print (sol.merge())