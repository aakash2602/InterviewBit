class Solution():

    def threePointers(self, A, B, C):
        p1 = 0
        p2 = 0
        p3 = 0
        min_value = 9223372036854775807
        while p1 <=len(A)-1 and p2 <= len(B)-1 and p3 <= len(C)-1:
            value1 = abs(A[p1] - B[p2])
            value2 = abs(B[p2] - C[p3])
            value3 = abs(C[p3] - A[p1])
            max_value = max(value1, value2, value3)
            min_value = min(min_value, max_value)
            print(f"{value1}::{value2}::{value3}::{max_value}::{min_value}::{p1}::{p2}::{p3}")
            if value1 == max_value:
                if A[p1] <= B[p2]:
                    p1 += 1
                elif A[p1] > B[p2]:
                    p2 += 1
            elif value2 == max_value:
                if B[p2] <= C[p3]:
                    p2 += 1
                elif B[p2] > C[p3]:
                    p3 += 1
            elif value3 == max_value:
                if C[p3] <= A[p1]:
                    p3 += 1
                elif C[p3] > A[p1]:
                    p1 += 1
        return min_value


if __name__ == "__main__":
    sol = Solution()
    print (sol.threePointers([1, 4, 10], [2, 15, 20], [10, 12]))