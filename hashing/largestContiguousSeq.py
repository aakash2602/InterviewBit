class Solution():

    def largestContiguousSeq(self, A):
        hash_map = {}
        max_len = 0
        max_len_elem = ()
        curr_sum = 0
        for i in range(len(A)):
            curr_sum += A[i]

            # print (f"{A[i]}:{curr_sum}::{max_len}:{max_len_elem}")

            if A[i] == 0 and max_len == 0:
                max_len = 1
                max_len_elem = (i, i)

            if curr_sum == 0:
                max_len = i + 1
                max_len_elem = (0, i)

            if curr_sum in hash_map:
                length = i - hash_map[curr_sum]
                if length > max_len:
                    max_len = length
                    max_len_elem = (hash_map[curr_sum]+1, i)
            else:
                hash_map[curr_sum] = i

        if max_len_elem:
            return A[max_len_elem[0]:max_len_elem[1]+1]
        else:
            return []

if __name__ == "__main__":
    sol = Solution()
    print (sol.largestContiguousSeq([8, -19, 8, 2, -8, 19, 5, -2, -23]))
    # print (sol.largestContiguousSeq([ -8, 8, -1, -16, -28, -27, 15, -14, 14, -27, -5, -6, -25, -11, 28, 29, -3, -25, 17, -25, 4, -20, 2, 1, -17, -10, -25 ]))
    # print (sol.largestContiguousSeq([ 22, -7, 15, -21, -20, -8, 16, -20, 5, 2, -15, -24, 19, 25, 3, 23, 18, 0, 16, 26, 13, 4, -20, -13, -25, -2 ]))