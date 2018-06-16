class Solution():

    def power(self, x, y, d):
        value = 1
        if y == 0:
            return 0
        x = x % d
        while y > 0:
            if y & 1:
                value = (value * x) % d

            y = y>>1
            x = (x*x)%d
            # print (f"{y} :: # x} :: {value}")
        return value

if __name__ == "__main__":
    sol = Solution()
    print (sol.power(2, 3, 3))