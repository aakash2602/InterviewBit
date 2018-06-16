class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer

    # def uniquePaths(self, A, B): ## This is recursion, it will be slow to TLE
    #     paths = self.get_paths(A - 1, B - 1)
    #     return paths
    #
    # def get_paths(self, A, B):
    #     print (f"{A}::{B}")
    #     if A < 0 or B < 0:
    #         return 0
    #     if A == 0 and B == 0:
    #         return 1
    #     val = self.get_paths(A, B - 1)
    #     val += self.get_paths(A - 1, B)
    #     return val

    ## DP code
    def uniquePaths(self, A, B):
        grid = [[0 for x in range(B)] for i in range(A)]
        for i in range(A):
            grid[i][0] = 1
        for i in range(B):
            grid[0][i] = 1
        for i in range(1, A):
            for j in range(1, B):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[A - 1][B - 1]

if __name__ == "__main__":
    sol = Solution()
    print (sol.uniquePaths(1, 3000))