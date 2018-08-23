class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        pos = self.binary_search(A, B)
        # print (pos)
        if pos == -1:
            return 0
        left_index = self.get_left_index(A, pos)
        print (left_index)
        right_index = self.get_right_index(A, pos)
        print(right_index)
        return right_index - left_index - 1

    def binary_search(self, A, B):
        start = 0
        end = len(A) - 1
        while start <= end:
            mid = int((start + end) / 2)
            if A[mid] > B:
                end = mid - 1
            elif A[mid] < B:
                start = mid + 1
            else:
                return mid
        return -1

    def get_left_index(self, A, pos):
        i = 0
        ref = pow(2, i)
        while pos - ref >= 0:
            new_pos = pos - ref
            print(new_pos)
            if A[new_pos] == A[pos]:
                i += 1
            else:
                break
            ref = pow(2, i)
        if i == 0:
            return pos - 1
        print (f"pow:: {i}::{pos}")

        for j in range(pow(2, i-1), pow(2, i) + 1):
            # print (j)
            # print (pos - j)
            print (f"{j} :: {pos-j}")
            if pos - j < 0:
                return -1
            if A[pos - j] != A[pos]:
                return pos - j
        return -1

    def get_right_index(self, A, pos):
        i = 0
        ref = pow(2, i)
        n = len(A)
        while pos + ref < n:
            new_pos = pos + ref
            # print(new_pos)
            if A[new_pos] == A[pos]:
                i += 1
            else:
                break
            ref = pow(2, i)
        if i == 0:
            return pos + 1
        for j in range(pow(2, i - 1), pow(2, i) + 1):
            if pos + j > n - 1:
                return n
            if A[pos + j] != A[pos]:
                return pos + j
        return n


if __name__ == "__main__":
    sol = Solution()
    print(sol.findCount([ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ], 10))