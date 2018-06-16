class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        a = [0] * 3
        for i in range(len(A)):
            a[A[i]] += 1
        A = []
        A = [0] * a[0]
        A.extend([1] * a[1])
        A.extend([2] * a[2])
        return A

if __name__ == "__main__":
    sol = Solution()
    print(sol.sortColors([0, 0, 1, 2, 1, 2]))