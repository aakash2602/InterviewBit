class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        mode = 0
        row_start = 0
        row_end = len(A)
        column_start = 0
        column_end = len(A[0])
        vector = []
        while row_start < row_end and column_start < column_end:
            if mode == 0:
                # vector.extend(A[row_start][column_start:column_end])
                for i in range(column_start, column_end):
                    vector.append(A[row_start][i])
                row_start += 1
                mode = 1
            elif mode == 1:
                # vector.extend(A[row_start:row_end][column_end-1])
                for i in range(row_start, row_end):
                    vector.append(A[i][column_end-1])
                column_end -= 1
                mode = 2
            elif mode == 2:
                # vector.extend(reversed(A[row_end - 1][column_start:column_end]))
                for i in range(column_end - 1, column_start - 1, -1):
                    vector.append(A[row_end - 1][i])
                row_end -= 1
                mode = 3
            elif mode == 3:
                # vector.extend(reversed(A[row_start:row_end][column_start]))
                for i in range(row_end - 1, row_start - 1, -1):
                    vector.append(A[i][column_start])
                column_start += 1
                mode = 0
            print (vector)
            print (row_start)
            print(row_end)
            print(column_start)
            print (column_end)
        return vector


if __name__ == "__main__":
    sol = Solution()
    A = [[1 ,2, 3], [4, 5, 6]]
    print (sol.spiralOrder(A))