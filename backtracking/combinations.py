class Solution():

    def combinations(self, A, B):
        seq = list(range(1, A + 1))
        out = []
        out.append([])
        out = self.comb(seq, B, 0, out)
        out_B = []
        for i in range(len(out)):
            if len(out[i]) == B:
                out_B.append(out[i])
        return out_B

    def comb(self, seq, B, index, out):
        if index >= len(seq):
            return out
        out = self.comb(seq, B, index + 1, out)
        new_out = []
        for i in range(len(out)):
            if len(out[i]) < B:
                temp = [seq[index]] + out[i]
                new_out.append(temp)

        out = [out[0]] + new_out + out[1:] if len(out) > 1 else [out[0]] + new_out
        # print (out)
        return out

    def comb1(self, seq, B, index, out):
        if index >= len(seq):
            return out
        out = self.comb(seq, B, index + 1, out)
        new_out = []
        for i in range(len(out)):
            if len(out[i]) < B:
                temp = [seq[index]] + out[i]
                new_out.append(temp)

        out = [out[0]] + new_out + out[1:] if len(out) > 1 else [out[0]] + new_out
        # print (out)
        return out

if __name__ == "__main__":
    sol = Solution()
    print (sol.combinations(4, 2))