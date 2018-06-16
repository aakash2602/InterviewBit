class Solution():

    def rotateMatrix(self, A):
        row_start = 0
        row_end = len(A) - 1
        col_start = 0
        col_end = len(A) - 1
        while row_start <= row_end:
            for i in range(0, col_end - col_start):
                print(f"row: {row_start}: {row_end}")
                print(f"col: {col_start}: {col_end}")
                temp = A[row_start][col_start + i]
                A[row_start][col_start + i] = A[row_end - i][col_start]
                A[row_end - i][col_start] = A[row_end][col_end - i]
                A[row_end][col_end - i] = A[row_start + i][col_end]
                A[row_start + i][col_end] = temp
                print (A)
            row_start += 1
            col_start += 1
            row_end -= 1
            col_end -= 1
        return A


if __name__ == "__main__":
    sol = Solution()
    print (sol.rotateMatrix([[1,2, 3,4, 5], [6, 7,8, 9, 10], [11,12, 13, 14, 15], [16, 17, 18, 19 , 20], [21, 22, 23, 24, 25]]))