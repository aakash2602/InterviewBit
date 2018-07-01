class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def Mod(self, A, B, C):
        if B == 0:
            return 1
        A = A % C
        val = self.mod(A, B, C)
        return val

    def mod(self, A, B, C):
        if B == 1:
            return A % C
        val = self.mod(A, B//2, C)
        val = (val * val) % C
        if B % 2 == 1:
            val = (val * A) % C
        return val

if __name__ == "__main__":
    sol = Solution()
    print (sol.Mod(71045970, 41535484, 64735492))