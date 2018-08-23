class Solution():

    def nearestSmallestElement(self, A):
        n = len(A)
        arr = []
        if n == 0:
            return arr
        arr.append(-1)
        stack = []
        stack.append(A[0])
        for i in range(1, n):
            print (stack)
            print (arr)
            if A[i] > stack[-1]:
                arr.append(stack[-1])
                stack.append(A[i])
            else:
                last = -1
                while stack and A[i] <= stack[-1]:
                    stack.pop()
                last = stack[-1] if stack else last
                arr.append(last)
                stack.append(A[i])
        return arr

if __name__ == "__main__":
    sol = Solution()
    print (sol.nearestSmallestElement([1, 2, 3, 4 ,5 ,6 ,7 ,8 ,9, 10]))
