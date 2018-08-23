class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        left_index = self.binary_search(A, B, 0)
        if left_index == -1:
            return [-1, -1]
        right_index = self.binary_search(A, B, 1)
        return [left_index, right_index]

    def binary_search(self, A, B, mode):
        start = 0
        end = len(A) - 1
        result = -1
        while start <= end:
            mid = int((start + end) / 2)
            if A[mid] > B:
                end = mid - 1
            elif A[mid] < B:
                start = mid + 1
            else:
                result = mid
                if mode == 0:
                    end = mid - 1
                elif mode == 1:
                    start = mid + 1
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))