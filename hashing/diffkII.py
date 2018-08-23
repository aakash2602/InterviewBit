class Solution():

    def diffK(self, A, B):
        num = {}
        n = len(A)
        for i in range(n):
            # print(A[i])
            # print(num)
            if B + A[i] in num:
                if num[B+A[i]] != i:
                    return 1
            if A[i] - B in num:
                if num[A[i]-B] != i:
                    return 1
            num[A[i]] = i
        return 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.diffK([ 34, 63, 64, 38, 65, 83, 50, 44, 18, 34, 71, 80, 22, 28, 20, 96, 33, 70, 0, 25, 64, 96, 18, 2, 53, 100, 24, 47, 98, 69, 60, 55, 8, 38, 72, 94, 18, 68, 0, 53, 18, 30, 86, 55, 13, 93, 15, 43, 73, 68, 29 ], 97))