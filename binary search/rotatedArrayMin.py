class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = int((start + end)/2)
            # print (mid)
            left_value = A[mid-1] if mid > 0 else A[mid] - 1
            right_value = A[mid+1] if mid < len(A) - 1 else A[mid] + 1
            if left_value > A[mid] and A[mid] < right_value:
                return A[mid]
            elif A[mid] >= A[0]:
                start = mid + 1
            elif A[mid] <= A[len(A)-1]:
                end = mid - 1
            else:
                return A[0]
        return A[0]

if __name__ == "__main__":
    sol = Solution()
    print (sol.findMin([1]))