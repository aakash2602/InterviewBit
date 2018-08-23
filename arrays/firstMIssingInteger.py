class Solution():

    def firstMissingInteger(self, A):
        index = 0
        for i in range(len(A)):
            if A[i] <= 0:
                A[index], A[i] = A[i], A[index]
                index += 1
        A = A[index:]
        print (A)
        if len(A) == 0:
            return 1
        for i in range(len(A)):
            if abs(A[i]) <= len(A):
                if A[abs(A[i]) - 1] > 0:
                    A[abs(A[i]) - 1] = -1 * A[abs(A[i]) - 1]
        print (A)
        for i in range(len(A)):
            if A[i] > 0:
                return i + 1
        return len(A) + 1

if __name__ == "__main__":
    sol = Solution()
    print (sol.firstMissingInteger([-8, -7 , -6, -5, 1, 2, 3]))