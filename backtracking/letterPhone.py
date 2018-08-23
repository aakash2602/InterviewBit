class Solution():

    def letterPhone(self, A):
        if len(A) == 0:
            return []

        d = {}
        d['0'] = ['0']
        d['1'] = ['1']
        d['2'] = ['a', 'b', 'c']
        d['3'] = ['d', 'e', 'f']
        d['4'] = ['g', 'h', 'i']
        d['5'] = ['j', 'k', 'l']
        d['6'] = ['m', 'n', 'o']
        d['7'] = ['[', 'q', 'r', 's']
        d['8'] = ['t', 'u', 'v']
        d['9'] = ['w', 'x', 'y', 'z']

        out = []
        out.append('')
        out = self.gen(A, 0, d, out)
        return out

    def gen(self, A, index, d, out):
        if index >= len(A):
            return out

        m = len(out)
        n = len(d[A[index]])
        new_out = []
        for j in range(m):
            for i in range(n):
                temp = []
                val = out[j][:]
                # print (val)
                # temp.append(d[A[index]][i])
                val = val + d[A[index]][i]
                # print (val)
                temp.append(val)
                temp = self.gen(A, index+1, d, temp)
                new_out.extend(temp)
        out = new_out
        return out

if __name__ == "__main__":
    sol = Solution()
    print (sol.letterPhone("23"))
