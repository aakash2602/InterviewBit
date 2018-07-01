class Solution():

    def evalExpression(self, A):
        stack = []
        oparr = ['+', '-', '*', '/']
        if len(A) == 0:
            return 0
        for elem in A:
            if elem in oparr:
                y = stack.pop()
                x = stack.pop()
                value = self.get_value(x, y, elem)
                stack.append(value)
            else:
                stack.append(elem)
        return stack.pop()


    def get_value(self, x, y, op):
        x = int(x)
        y = int(y)
        if op == '+':
            return str(x+y)
        elif op == '-':
            return str(x-y)
        elif op == '*':
            return str(x*y)
        elif op == '/':
            return str(x//y)

if __name__ == "__main__":
    sol = Solution()
    print (sol.evalExpression())