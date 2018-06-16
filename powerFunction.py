class Solution():

    def power(self, A, n):
        if A == 0:
            return 0
        if n == 0:
            return 1
        temp = self.power(A, int(n/2))
        if n & 1:
            result = A * temp * temp
        else:
            result = temp * temp
        print (f"{temp}::{result}::{n}")
        return result

if __name__ == "__main__":
    sol = Solution()
    print (sol.power(10, 10))