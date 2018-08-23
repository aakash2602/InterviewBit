class Solution():

    def minimizeDifference(self, A, B, C):
        p1 = 0
        p2 = 0
        p3 = 0
        abs_min_value = 9223372036854775807
        while p1 <= len(A) - 1 and p2 <= len(B) - 1 and p3 <= len(C) - 1:
            max_value = max(A[p1], B[p2], C[p3])
            min_value = min(A[p1], B[p2], C[p3])
            abs_min_value = min(abs_min_value, max_value-min_value)
            print (f"{max_value}::{min_value}::{p1}::{p2}::{p3}::{abs_min_value}")
            if min_value == A[p1]:
                p1 += 1
            elif min_value == B[p2]:
                p2 += 1
            elif min_value == C[p3]:
                p3 += 1
        return abs_min_value

if __name__ == "__main__":
    sol = Solution()
    print (sol.minimizeDifference([ -1 ], [ -2 ], [ -3 ]))