class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        neg = 1 if A < 0 else 0
        A = str(abs(A))
        A = int(A[::-1])
        if A > 2**31 - 1:
            return 0
        if neg:
            return -A
        else:
            return A

if __name__ == "__main__":
    sol = Solution()
    print (sol.reverse(676))