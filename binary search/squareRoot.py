class Solution():

    def squareRoot(self, A):
        start = 0
        end = A
        result = -1
        while start <= end:
            mid = int((start+end)/2)
            square_value = pow(mid, 2)
            print (f"{mid} :: {square_value}")
            if square_value == A:
                return mid
            elif square_value < A:
                result = mid
                start = mid + 1
            else:
                end = mid - 1
        return int(result)

if __name__ == "__main__":
    sol = Solution()
    print (sol.squareRoot(10))