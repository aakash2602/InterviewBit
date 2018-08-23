class Solution():

    def kthpermutation(self, A, B):
        arr = list(range(1, A+1))
        result = []
        fact = self.get_fact(A-1)
        self.get_kthp(arr, B-1, [], fact, result)
        result = [str(val) for val in result]
        result = ''.join(result)
        return result

    def get_kthp(self, A, B, temp, fact, result):
        n = len(A)
        if n == 0:
            # out.append(temp)
            result.extend(temp)
            return
        # print (A)
        # print (fact)
        val = (B)//fact
        temp.append(A[val])
        A.pop(val)
        if n > 1:
            self.get_kthp(A, (B)%fact, temp, fact//(n-1), result)
        else:
            result.extend(temp)

        return

    def get_fact(self, n):
        num = 1
        for i in range(2, n+1):
            num *= i
        return num

if __name__ == "__main__":
    sol = Solution()
    print (sol.kthpermutation(11, 14))