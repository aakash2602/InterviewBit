class Solution():

    def zigzagString(self, A, B):
        n = len(A)
        if n == 0:
            return ""
        if B == 1:
            return A
        out = ''
        for i in range(1, B+1):
            index = i - 1
            out += A[index] if index < n else ''
            mode = 0 ## 0 means down, 1 means up
            next = -1
            while index < n:
                if mode == 0:
                    next = (B - i - 1) * 2 + 1 + 1
                    mode = 1
                elif mode == 1:
                    next = (i - 1 - 1) * 2 + 1 + 1
                    mode = 0
                print(f"{index}:{A[index]}::{i}:{mode}::{next}:{n}")
                if next > 0:
                    index += next
                    out = out + A[index] if index < n else out
                    # out += A[index]
        return out

if __name__ == "__main__":
    sol = Solution()
    print (sol.zigzagString("PAYPALISHIRING", 5))