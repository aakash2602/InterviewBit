class Solution():

    def parenthesis(self, A):
        out = []
        temp = ''
        self.get(A, 0, temp, out)
        return out

    def get(self, A, sum, temp, out):
        if len(temp) == A*2 and sum == 0:
            out.append(temp)
        elif len(temp) > A*2 or sum < 0:
            return

        # print (temp)

        if sum == A:
            new_temp = temp[:]
            new_temp += ')'
            sum -= 1
            self.get(A, sum, new_temp, out)
        else:
            new_temp = temp[:]
            self.get(A, sum+1, new_temp+'(', out)
            if new_temp != '':
                self.get(A, sum-1, new_temp+')', out)

if __name__ == "__main__":
    sol = Solution()
    print (sol.parenthesis(3))

