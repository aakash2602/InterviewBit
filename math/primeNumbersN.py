class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        a = [0] * (A + 1)
        primes = []
        for i in range(2, A + 1):
            if a[i] == 0:
                primes.append(i)
                a[i] += 1
                j = 2
                while i * j <= A:
                    print (i*j)
                    a[i * j] += 1
                    j += 1

        return primes

if __name__ == "__main__":
    sol = Solution()
    print (sol.sieve(5))