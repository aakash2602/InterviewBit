class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        value = 0
        n = len(A)
        for i in range(n):
            value += pow(26, n-1-i) * (ord(A[i]) - 64)
        return value

if __name__ == "__main__":
    sol = Solution()
    print (sol.titleToNumber(''))