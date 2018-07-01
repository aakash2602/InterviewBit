class Solution():

    def combSum(self, A, B):
        out = []
        # self.get_comb(A, B, 0, temp, out, sum_out)
        self.get_comb(A, 0, B, [], out)
        return out

    def get_comb1(self, A, B, index, temp, out, sum_out):
        if index >= len(A):
            return
        if A[index] <= B:
            if A[index] == B:
                out.append([A[index]])
            else:
                new = []
                i = 0
                # for i in range(len(temp)):
                print (sum_out)
                print (temp)
                print (A[index])
                while i < len(temp):
                    if temp[i][-1] > A[index]:
                        i += 1
                        continue
                    if sum_out[i] + A[index] < B:
                        new_temp = temp[i].copy()
                        new_temp.append(A[index])
                        # temp.append(new_temp)
                        temp.insert(i, new_temp)
                        sum_out.insert(i, sum_out[i] + A[index])
                        i += 1
                        # sum_out[i] += A[index]
                    elif sum_out[i] + A[index] == B:
                        new_temp = temp[i].copy()
                        new_temp.append(A[index])
                        temp.insert(i, new_temp)
                        sum_out.insert(i, B)
                        i += 1
                        # out.append(new_temp)
                    i += 1
                temp.append([A[index]])
                sum_out.append(A[index])
        self.get_comb1(A, B, index + 1, temp, out, sum_out)

    def get_comb(self, A, index, sum, arr, res):
        if sum < 0:
            return

        if sum == 0:
            if arr not in res:
                res.append(arr)
            return

        for i in range(index, len(A)):
            temp = arr[:]
            if len(temp) == 0:
                temp.append(A[i])
            else:
                n = len(temp)
                j = 0
                while j < n:
                    if A[i] <= temp[j]:
                        temp.insert(j, A[i])
                        break
                    j += 1
                if j == n:
                    temp.insert(n, A[i])
            # print (temp)
            self.get_comb(A, i+1, sum - A[i], temp, res)

if __name__ == "__main__":
    sol = Solution()
    print (sol.combSum([ 8, 10, 6, 11, 1, 16, 8 ], 28))
    # print(sol.combSum([10, 1, 2, 7, 6, 1, 5], 8))

## 228116