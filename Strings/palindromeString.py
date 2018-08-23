class Solution():

    def palindromeString(self, A):

        left = 0
        right = len(A) - 1
        A = A.lower()
        while right > left:
            # print (f"{left} :: {right} :: {A[left]} :: {A[right]}")
            l = A[left]
            r = A[right]
            if not l.isalnum():
                left += 1
                continue
            if not r.isalnum():
                right -= 1
                continue
            if A[left] != A[right]:
                return 0
            left += 1
            right -= 1
        return 1

if __name__ == "__main__":

    sol = Solution()
    print (sol.palindromeString("race a car"))