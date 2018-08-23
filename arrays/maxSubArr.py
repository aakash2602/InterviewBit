class Solution:
    def maxSubArray(self, A):
        max_sum = -9223372036854775808
        last_sum = 0
        for i in range(len(A)):
            last_sum += A[i]
            if max_sum < last_sum:
                max_sum = last_sum
            if last_sum < 0:
                last_sum = 0
        return  max_sum

if __name__ == "__main__":
    sol = Solution()
    print (sol.maxSubArray([-2, -123]))