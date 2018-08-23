class Solution():

    def redundantBraces(self, A):
        stack = []
        n = len(A)
        for i in range(n):
            if A[i] == ')':
                operator = 0
                last = stack.pop()
                while len(stack) != 0 and last != '(':
                    if last in ['+', '-', '/', '*']:
                        operator += 1
                    last = stack.pop()
                if operator == 0:
                    return 1
            else:
                stack.append(A[i])
        return 0

if __name__ == "__main__":
    sol = Solution()
    print (sol.redundantBraces("(a + (a + b))"))