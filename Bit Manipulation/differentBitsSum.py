class Solution():

    def differentBitsSum(self, A):
        num = 0

        n = len(A)
        mod_num = pow(10, 9) + 7
        for i in range(32):
            count = 0
            for j in range(n):
                if A[j] & (1 << i):
                    count += 1
            num = (num + (count * (n - count) * 2)) % (mod_num)

        return num

if __name__ == "__main__":
    sol = Solution()
    print (sol.differentBitsSum([1, 3, 5]))