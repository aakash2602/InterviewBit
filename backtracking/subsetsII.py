class Solution():

    def subsets(self, A):
        out = []
        out.append([])
        A.sort()
        self.subset(A, 0, out)
        out.sort()
        return out


    def subset(self, A, index, out):
        print (index)
        print (out)
        if index >= len(A):
            return

        n = len(out)
        for i in range(n):
            temp = out[i][:]
            temp.append(A[index])
            if temp not in out:
                out.append(temp)
        self.subset(A, index + 1, out)

if __name__ == "__main__":
    sol = Solution()
    print (sol.subsets([1,2,2]))