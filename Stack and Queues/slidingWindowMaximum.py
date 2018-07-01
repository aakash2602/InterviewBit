class Solution():

    def slidingWindowMax(self, A, B):
        stack = []
        out = []
        n = len(A)
        if n == 0:
            return []
        if B > len(A):
            return [max(A)]
        for i in range(B):
            while stack and A[i] >= A[stack[-1]]:
                stack.pop()
            stack.append(i)
        out.append(A[stack[0]])
        for i in range(B, n):
            print (stack)
            if stack[0] <= i - B:
                stack.pop(0)
            while stack and A[i] >= A[stack[-1]]:
                stack.pop()
            stack.append(i)
            out.append(A[stack[0]])
        return out

if __name__ == "__main__":
    sol = Solution()
    print (sol.slidingWindowMax([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 3))