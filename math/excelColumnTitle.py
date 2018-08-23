class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        value = ''
        A = A
        while A > 0:
            mod = A%26
            if mod == 0:
                value += 'Z'
                A = int(A/26) - 1
            else:
                value += chr(mod + 64)
                A = int(A/26)
                # print (A)
        return value[::-1]

if __name__ == "__main__":
    sol = Solution()
    print (sol.convertToTitle(676))