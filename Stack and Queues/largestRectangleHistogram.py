class Solution():

    def largestRectangleHist(self, A):
        n = len(A)
        if n == 0:
            return 0
        stack = []
        stack.append(0)
        area = A[0]
        i = 1
        while i < n:
            print (stack)
            if not stack or A[i] >= A[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                if stack:
                    length = i - stack[-1] - 1
                else:
                    length = i
                area_val = A[top] * length
                if area_val > area:
                    area = area_val
        while stack:
            top = stack.pop()
            if stack:
                length = i - stack[-1] - 1
            else:
                length = i
            area_val = A[top] * length
            if area_val > area:
                area = area_val
        return area

    def largestRectangleArea(self, A):
        rectangle_stack = []
        max_value = 0
        index = 0
        while index < len(A):
            print (rectangle_stack)
            if not rectangle_stack or A[index] >= A[rectangle_stack[-1]]:
                rectangle_stack.append(index)
                index += 1
            else:
                top = rectangle_stack[-1]
                rectangle_stack.pop(len(rectangle_stack) - 1)
                if not rectangle_stack:
                    length = index
                else:
                    length = index - rectangle_stack[-1] - 1
                area = A[top] * length
                if max_value < area:
                    max_value = area
        while rectangle_stack:
            top = rectangle_stack[-1]
            rectangle_stack.pop(len(rectangle_stack) - 1)

            if not rectangle_stack:
                length = index
            else:
                length = index - rectangle_stack[-1] - 1
            area = A[top] * length
            if max_value < area:
                max_value = area

        return max_value

if __name__ == "__main__":
    sol = Solution()
    print (sol.largestRectangleHist([2,4,4,5,3]))
    print(sol.largestRectangleArea([2, 4, 4, 5, 3]))