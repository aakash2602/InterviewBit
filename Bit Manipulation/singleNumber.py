class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        xor = 0
        for i in range(len(A)):
            xor = xor^A[i]
        return xor