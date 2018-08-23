class Solution():

    def maximumGap(self, A):
        max_diff = -1
        Lmin = [A[i] for i in range(len(A))]
        for i in range(1, len(A)):
            Lmin[i] = min(A[i], Lmin[i - 1])
        Rmax = [A[i] for i in range(len(A))]
        for i in range(len(A) - 2, -1, -1):
            Rmax[i] = max(A[i], Rmax[i + 1])
        l_index = 0
        r_index = 0
        while l_index < len(A) and r_index < len(A):
            if Lmin[l_index] > Rmax[r_index]:
                l_index += 1
            else:
                max_diff = max(max_diff, r_index - l_index)
                r_index += 1
        return max_diff

if __name__ == "__main__":
    sol = Solution()
    print (sol.maximumGap([]))