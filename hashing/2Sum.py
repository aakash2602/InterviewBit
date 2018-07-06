class Solution():

    def TwoSum(self, A, B):
        hash_map = {}
        out = []
        for i in range(len(A)):

            if B-A[i] in hash_map:
                out.extend([hash_map[B-A[i]]+1, i+1])
                break

            if A[i] not in hash_map:
                hash_map[A[i]] = i
        return out

if __name__ == "__main__":
    sol = Solution()
    print (sol.TwoSum([2, 2, 2, 7, 7, 11, 15], 119))