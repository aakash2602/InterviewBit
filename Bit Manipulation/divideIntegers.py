class Solution():

    def divide(self, A, B):
        temp = 0
        value = 0
        if (A < 0 and B < 0) or (A > 0 and B > 0):
            neg = 1
        else:
            neg = -1
        A = abs(A)
        B = abs(B)
        for i in range(31, -1, -1):
            print (f"{temp + (B << i)} :::: {B}")
            if temp + (B << i) <= A:
                temp += B << i
                value += 1 << i
            print (f"{i} :: {value}")
        value = neg * value
        if value > 2147483647 or value < -2147483648:
            value = 2147483647
        return value

if __name__ == "__main__":
    sol = Solution()
    print (sol.divide(-1, 1))