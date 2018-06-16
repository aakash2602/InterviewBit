class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        count = 0
        row = len(A)
        column = len(A[0])
        B = [[1 for col in each_row] for each_row in A]
        for i in range(row):
            for j in range(column):
                # print (A[i][j])
                if A[i][j] == 'X' and B[i][j] == 1:
                    count += 1
                    self.get_path(i, j, A, B)
        return count


    def get_path(self, row, column, A, B):
        if row < 0 or row >= len(A) or column < 0 or column >= len(A[0]) or A[row][column] != 'X' or B[row][column] != 1:
            return
        B[row][column] = 0
        self.get_path(row + 1, column, A, B)
        self.get_path(row - 1, column, A, B)
        self.get_path(row, column - 1, A, B)
        self.get_path(row, column + 1, A, B)
        return

if __name__ == "__main__":
    sol = Solution()
    A = [['X','X', 'X'], ['X', 'X','X'] , ['X', 'X', 'X']]
    print (sol.black(A))