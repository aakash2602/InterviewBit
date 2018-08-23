class Solution():

    def threeSum(self, A, B):
        A.sort()
        n = len(A)
        min_value = 9223372036854775807
        real_value = 0
        for i in range(n):
            start = 0 if i != 0 else 1
            end = n - 1 if i != n-1 else n-2
            value = B - A[i]
            while end > start:
                new_value = A[start] + A[end]
                # print (f"{start}::# end}::{i}::{min_value}")
                score = new_value - value
                if new_value > value:
                    if abs(score) < min_value:
                        real_value = score + B
                        min_value = abs(score)
                    # min_value = min(abs(new_value + A[i] - B), min_value)
                    end -= 1
                elif new_value < value:
                    if abs(score) < min_value:
                        real_value = score + B
                        min_value = abs(score)
                    # min_value = min(new_value + A[i] - B, min_value)
                    start += 1
                else:
                    return B
                start = start + 1 if start == i else start
                end = end - 1 if end == i else end
        return real_value

if __name__ == "__main__":
    sol = Solution()
    print (sol.threeSum([ 2, 1, -9, -7, -8, 2, -8, 2, 3, -8 ], -1))