class Solution():

    def addBinaryStrings(self, A, B):
        n = len(A)
        m = len(B)
        length = max(n, m)
        carry = 0
        sum = ''
        for i in range(length):
            val1 = int(A[n-1-i]) if n-1-i >= 0 else 0
            val2 = int(B[m-1-i]) if m-1-i >= 0 else 0
            sum_value = val1 + val2 + carry
            sum += str(sum_value%2)
            carry = sum_value//2
        sum = sum + '1' if carry == 1 else sum
        return sum[::-1]

if __name__ == "__main__":
    sol = Solution()
    print (sol.addBinaryStrings("11" , "11111111"))