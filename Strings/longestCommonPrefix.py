class Solution():

    def lcp(self, A):
        prefix = ''
        index = 0
        n = len(A[0])
        while True:
            if index < n:
                letter = A[0][index]
            else:
                return prefix
            for i in range(1, len(A)):
                m = len(A[i])
                if index >= m:
                    return prefix
                if A[i][index] != letter:
                    return prefix
            prefix += letter
            index += 1
        return prefix

if __name__ == "__main__":
    sol = Solution()
    print (sol.lcp([

  "abc",

  "a",

  "abc"
]))

