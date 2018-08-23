class Solution:

    def generateMatrix(self, A):
        seq = [i for i in range(1, pow(A, 2) + 1)]
        print (seq)
        row_start = 0
        row_end = A
        column_start = 0
        column_end = A
        mode = 0
        B = [[0 for col in range(A)] for each_row in range(A)]
        while seq:
            print (f"row: {row_start}: {row_end}")
            print(f"col: {column_start}: {column_end}")
            if mode == 0:
                seq_length = column_end - column_start
                seq_intd = seq[:seq_length]
                index = 0
                for i in range(column_start, column_end):
                    B[row_start][i] = seq_intd[index]
                    index += 1
                row_start += 1
                mode = 1
            elif mode == 1:
                seq_length = row_end - row_start
                print (seq_length)
                seq_intd = seq[:seq_length]
                index = 0
                for i in range(row_start, row_end):
                    B[i][column_end - 1] = seq_intd[index]
                    index += 1
                column_end -= 1
                mode = 2
            elif mode == 2:
                seq_length = column_end - column_start
                seq_intd = seq[:seq_length]
                index = 0
                for i in range(column_end - 1, column_start - 1, -1):
                    B[row_end - 1][i] = seq_intd[index]
                    index += 1
                row_end -= 1
                mode = 3
            elif mode == 3:
                seq_length = row_end - row_start
                seq_intd = seq[:seq_length]
                index = 0
                for i in range(row_end - 1, row_start - 1, -1):
                    B[i][column_start] = seq_intd[index]
                    index += 1
                column_start += 1
                mode = 0
            seq = seq[seq_length:]
            print (seq)
            print (B)
        return B

if __name__ == "__main__":
    sol = Solution()
    print (sol.generateMatrix(5))