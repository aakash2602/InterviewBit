class Solution():
    def generate(self, A):
        if A < 1:
            return 
        B = []
        B.append([1])
        for row in range(1, A):
            col_value = []
            for col in range(row+1):
                value = 0
                if col + 1 <= row:
                    value += B[row - 1][col]
                if col - 1 >= 0:
                    value += B[row - 1][col - 1]
                col_value.append(value)
            B.append(col_value)
        return B


if __name__ == "__main__":
    sol = Solution()
    print (sol.generate(0))