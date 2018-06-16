class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        value = 0
        for i in range(31, -1, -1):
            if A == 0:
                break
            if A & 1:
                value += pow(2, i)
            A = A >> 1
        return value