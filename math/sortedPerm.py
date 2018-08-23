class Solution():

    def sortedPermRank(self, A):
        arr = [letter for letter in A]
        arr.sort()
        n = len(A)
        fact = self.get_fact(n-1)
        num = 1
        for i in range(n-1):
            # print (fact)
            pos = arr.index(A[i])
            num += abs(pos) * fact #if pos-i > 0 else 0
            # print (num)
            # print (pos)
            arr.pop(pos)
            if n-1-i > 0:
                fact = fact // (n-1-i)
        return num % 1000003

    def get_fact(self, n):
        num = 1
        for i in range(2, n+1):
            num *= i
        return num

if __name__ == "__main__":
    sol = Solution()
    print (sol.sortedPermRank("DTNGJPURFHYEW"))