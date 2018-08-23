class Solution():

    def diff(self, A, B):
        start = 0
        end = 1
        while end < len(A):
            value = A[end] - A[start]
            print (f"{start}::{end}::{value}")
            if value == B:
                return 1
            elif value > B:
                if start != end - 1:
                    start += 1
                else:
                    end += 1
            elif value < B:
                end += 1
        return 0

if __name__ == "__main__":
    sol = Solution()
    print (sol.diff([ 1, 2, 2, 3, 4 ], 0))