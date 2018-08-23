class Solution():

    def remove_element(self, A, B):
        n = len(A)
        start = 0
        length = 0
        last = 0
        while start < n:
            if A[start] == B:
                # A.pop(start)
                # n -= 1
                start += 1
            else:
                A[last] = A[start]
                start += 1
                length += 1
                last += 1
        A = A[:length]
        # print (A)
        return length

if __name__ == "__main__":
    sol = Solution()
    print(sol.remove_element([4, 1, 1, 2, 1, 3], 1))