class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        row = len(A)
        column = len(A[0])
        if A[0][0] == 1:
            return 0
        for i in range(row):
            for j in range(column):
                if i == 0 and j == 0:
                    A[i][j] = 1
                    continue
                if A[i][j] == 1:
                    A[i][j] = 0
                    continue
                top_val = 0 if j - 1 < 0 else A[i][j - 1]
                left_val = 0 if i - 1 < 0 else A[i - 1][j]
                A[i][j] = top_val + left_val
        return A[row - 1][column - 1]

if __name__ == "__main__":
    sol = Solution()
    print (sol.uniquePathsWithObstacles(1, 3000))