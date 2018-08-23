class Solution():

    def colorful(self, A):
        dict = {}
        index = 1
        A = str(A)
        n = len(A)
        while index <= n:
            i = 0
            while i+index <= n:
                num = A[i:i+index]
                # print (num)
                val = 1
                for nu in num:
                    val *= int(nu)
                if val in dict:
                    return 0
                # print (val)
                dict[val] = 1
                i += 1
            index += 1
        return 1

if __name__ == "__main__":
    sol = Solution()
    print (sol.colorful(3255))