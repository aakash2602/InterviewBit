class Solution():

    def compareVersions(self, A, B):
        a = A.split('.')
        b = B.split('.')
        n = len(a)
        m = len(b)
        for i in range(n):
            if i >= m:
                if int(a[i]) == 0:
                    return 0
                else:
                    return 1
            val1 = int(a[i])
            val2 = int(b[i])
            if val1 > val2:
                return 1
            elif val1 < val2:
                return -1
        if m > n:
            if int(b[m-1]) == 0:
                return 0
            else:
                return -1
        else:
            return 0

if __name__ == "__main__":
    sol = Solution()
    print (sol.compareVersions("1.13", "1.13.4"))