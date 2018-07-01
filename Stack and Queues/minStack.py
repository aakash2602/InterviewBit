class MinStack:
    def __init__(self):
        self.stack = []
        self.min_value = []

    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        if not self.min_value:
            self.min_value.append(x)
        else:
            min_value = min(x, self.min_value[-1])
            if min_value == x:
                self.min_value.append(x)

    # @return nothing
    def pop(self):
        if self.stack:
            y = self.stack.pop()
            if y == self.min_value[-1]:
                self.min_value.pop()

    # @return an integer
    def top(self):
        if not self.stack:
            return -1
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        if not self.stack:
            return -1
        return self.min_value[-1]