class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        index = self.binary_search(A, B)
        return index

    def binary_search(self, A, B):
        start = 0
        end = len(A) - 1
        mid = 0
        while start <= end:
            mid = int((start + end) / 2)
            if A[mid] > B:
                end = mid - 1
            elif A[mid] < B:
                start = mid + 1
            else:
                return mid
        if A[mid] >= B:
            return mid
        elif A[mid] < B:
            return mid + 1

if __name__ == "__main__":
    sol = Solution()
    print (sol.searchInsert([1, 2, 3, 5], 4))