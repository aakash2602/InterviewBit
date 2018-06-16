class Solution():

    def intersection(self, A, B):
        pointer1 = 0
        pointer2 = 0
        intersection = []
        while pointer1 < len(A) and pointer2 < len(B):
            if A[pointer1] < B[pointer2]:
                pointer1 += 1
            elif A[pointer1] > B[pointer2]:
                pointer2 += 1
            elif A[pointer1] == B[pointer2]:
                intersection.append(A[pointer1])
                pointer1 += 1
                pointer2 += 1
        return intersection

if __name__ == "__main__":
    sol = Solution()
    print (sol.intersection([ -4, -2, 3 ], [ -2, -2 ]))