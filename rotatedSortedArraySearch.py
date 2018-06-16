class Solution():

    def array_search(self, A, B):
        if not A:
            return -1
        pivot = self.find_pivot(A)
        print (pivot)
        A1 = A[:pivot]
        A2 = A[pivot:]
        print (A1)
        print (A2)
        index = self.binary_search(A1, B)
        print (index)
        if index == -1:
            index = self.binary_search(A2, B)
            index = pivot + index if index != -1 else index

        return index

    def find_pivot(self, A):
        left = 0
        right = len(A)-1
        while (left<right):
            print (f"{left} :: {right}")
            mid = int((left + right + 1)/2)
            left_value = A[mid - 1] if mid > 0 else A[mid] - 1
            right_value = A[mid + 1] if mid < len(A) - 1 else A[mid] - 1
            if left_value < A[mid] > right_value:
                return mid + 1
            elif left_value < A[mid] < right_value:
                if A[mid] > A[0]:
                    left = mid
                elif A[mid] < A[0]:
                    right = mid
            elif left_value > A[mid] < right_value:
                return mid
        return 0

    def binary_search(self, A, B):
        left = 0
        right = len(A) - 1
        while left <= right:
            mid = int((left + right + 1)/2)
            if A[mid] > B:
                right = mid - 1
            elif A[mid] < B:
                left = mid + 1
            else:
                return mid
        return -1

if __name__ == "__main__":
    sol = Solution()
    print (sol.array_search([4,5,6,7,8,9,10,1,2,3], 2))