class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        a = [1] * (A+1)
        a[0] = 0
        a[1] = 0
        for i in range(2, int(A**0.5)+1):
            if a[i] == 1:
                # a[i] = 1
                j = 2
                while i*j <= A:
                    a[i*j] = 0
                    j += 1
        for i in range(A):
            if a[i] and a[A-i]:
                return [i, A-i]
        return -1


if __name__ == "__main__":
    sol = Solution()
    print (sol.primesum(16777214))