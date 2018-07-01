class Solution():

    def palindromPart(self, A):
        out = []
        temp = []
        self.plainPart(A, 0, temp, out)
        return out

    def plainPart(self, A, index, temp, out):
        if index == len(A):
            out.append(temp)

        n = len(A)
        for i in range(index+1, n+1):
            new_temp = temp[:]
            val = A[index:i]
            if not self.palinCheck(val):
                continue

            new_temp.append(val)
            self.plainPart(A, i, new_temp, out)


    def palinCheck(self, val):
        n = len(val) - 1
        i = 0
        while i < n:
            if val[i] != val[n]:
                return False
            i += 1
            n -= 1
        return True

if __name__ == "__main__":
    sol = Solution()
    print (sol.palindromPart("aab"))
