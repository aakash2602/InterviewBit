class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        factors = []
        factors_from_right = []
        for i in range(1, int(A**0.5)+1):
            if A%i == 0:
                factors.append(i)
                if i != int(A/i):
                    factors_from_right.append(int(A/i))
        factors = factors_from_right + list(reversed(factors))
        print (factors)
        for factor in factors:
            if B%factor == 0:
                return factor
        return 0


if __name__ == "__main__":
    sol = Solution()
    print (sol.gcd(4, 6))