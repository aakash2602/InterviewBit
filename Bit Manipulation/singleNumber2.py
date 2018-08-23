class Solution():

    def single_number(self, A):
        num = 0

        for i in range(32):
            count = 0
            for j in range(len(A)):
                if A[j] & (1 << i):
                    count += 1
            num += (count % 3) << i

        return num

if __name__ == "__main__":
    sol = Solution()
    print (sol.single_number([1, 2, 3, 4, 4, 4, 2, 2, 3, 3]))