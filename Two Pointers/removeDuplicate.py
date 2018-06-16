class Solution():

    def remove_duplicate(self, A):
        n = len(A)
        start = 1
        length = 1
        last = 1
        while start < n:
            if A[start] == A[start-1]:
                # A.pop(start)
                # n -= 1
                start += 1
            else:
                A[last] = A[start]
                start += 1
                length += 1
                last += 1
        A = A[:length]
        print (A)
        return length

if __name__ == "__main__":
    sol = Solution()
    print (sol.remove_duplicate([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ]))