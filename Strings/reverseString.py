class Solution():

    def reverseString(self, A):
        words = []
        last = ''
        n = len(A)
        for i in range(n):
            if A[i] == ' ':
                if last != '':
                    words.append(last)
                last = ''
                continue
            last += A[i]
        if last != '':
            words.append(last)
        word_length = len(words)
        output = ''
        for i in range(word_length-1, -1, -1):
            output += ' ' + words[i]
        return output.strip()

if __name__ == "__main__":
    sol = Solution()
    print (sol.reverseString("   the   sky blue         "))