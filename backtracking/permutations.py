class Solution():

    def permutations(self, A):
        out = []
        self.get_p(A, [], out)
        return out

    def get_p(self, A, temp, out):
        n = len(A)
        if n == 0:
            out.append(temp)
            return

        for i in range(n):
            new_arr = A[:]
            new_temp = temp[:]
            new_temp.append(A[i])
            new_arr.pop(i)
            self.get_p(new_arr, new_temp, out)

if __name__ == "__main__":
    sol = Solution()
    print (sol.permutations([1,2,3,4]))