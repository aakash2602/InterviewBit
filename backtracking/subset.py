class Solution():

    def subset(self, A):
        out = []
        A.sort()
        out.append([])
        self.get_all_subsets(A, 0, out)
        return out

    def get_all_subsets(self, A, index, out):
        if index >= len(A):
            return
        self.get_all_subsets(A, index + 1, out)
        new_out = []
        for i in range(len(out)):
            temp = out[i].copy()
            temp = [A[index]] + temp
            new_out.append(temp)
        for i in range(len(new_out)-1, -1, -1):
            out.insert(1, new_out[i])

    def subsets(self, A):
        # print '\nSubsets of', A
        S = sorted(A)
        out = []
        out.append([])
        for sset in self.subsets_generator(S):
            out.append(sset)
        return out

    def subsets_generator(self, S):
        if len(S) == 1:
            yield S
        else:
            for i in range(len(S)):
                ch = S[i]
                yield [ch]
                if S[i + 1:]:
                    for other in self.subsets_generator(S[i + 1:]):
                        yield [ch] + other

if __name__ == "__main__":
    sol = Solution()
    print (sol.subset([1,2,3]))
