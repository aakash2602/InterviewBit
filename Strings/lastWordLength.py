class Solution():

    def lastWordLength(self, A):
        n = len(A)
        last = ''
        word = ''
        for i in range(n):
            if A[i] == ' ':
                word = last if last != '' else word
                last = ''
                continue
            last += A[i]
        if last != '':
            word = last
        return len(word)

if __name__ == "__main__":
    sol = Solution()
    print (sol.lastWordLength("Hello World  "))