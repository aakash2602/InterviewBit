class Solution():

    def romanToInteger(self, A):
        n = len(A)
        total = 0
        i = 0
        while i < n:
            value = self.get_value(A[i])
            if i < n-1:
                next_value = self.get_value(A[i+1])
                if next_value > value:
                    total += next_value - value
                    i += 2
                    continue
            total += value
            i += 1
        return total

    def get_value(self, sym):
        if sym == 'I':
            return 1
        elif sym == 'V':
            return 5
        elif sym == 'X':
            return 10
        elif sym == 'L':
            return 50
        elif sym == 'C':
            return 100
        elif sym == 'D':
            return 500
        elif sym == 'M':
            return 1000

if __name__ == "__main__":
    sol = Solution()
    print (sol.romanToInteger(""))