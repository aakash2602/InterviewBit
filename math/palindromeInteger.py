class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        A = str(A)
        n = len(A)
        for i in range(int(n/2)):
            if A[i] != A[n-1-i]:
                return 0
        return 1