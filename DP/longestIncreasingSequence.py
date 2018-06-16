class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        seq = [1] * len(A)

        ## DP O(n*n)
        for i in range(len(A)):
            for j in range(i):
                if A[i] > A[j] and seq[j] + 1 > seq[i]:
                    seq[i] = seq[j] + 1

        return max(seq)

if __name__ == "__main__":
    sol = Solution()
    print (sol.lis([50, 3, 10, 72, 40, 80]))