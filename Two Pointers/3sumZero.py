class Solution():

    def threeSumZero(self, A):
        A.sort()
        triplets = []
        n = len(A)
        for i in range(n-1):
            start = i + 1
            end = n-1
            while end > start:
                score = A[i] + A[start] + A[end]
                if score == 0:
                    if (A[i], A[start], A[end]) not in triplets:
                        triplets.append((A[i], A[start], A[end]))
                    start += 1
                    end -= 1
                elif score > 0:
                    end -= 1
                elif score < 0:
                    start += 1
        return triplets

if __name__ == "__main__":
    sol = Solution()
    print (sol.threeSumZero([-1, 0, 1, 2, -1, -4]))