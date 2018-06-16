class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        combinations = 0
        for j in range(len(A)):
            if A[j] == 0:
                continue
            if A[j] < C[0]:
                combinations += pow(len(A), B-1)
                continue
            if A[j] == C[0]:
                comb = 1
                # for i in range(1, B):
                #     for k in range(len(A)):
