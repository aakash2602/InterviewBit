class Solution():

    def minCharsToMakePalindromic(self, A):
        n = len(A) - 1
        if n < 0:
            return 0
        start = 0
        end = n
        last = -1
        length = 0
        local_index = (-1, -1)
        while end >= start:
            print (f"{start}:{A[start]}::{end}:{A[end]}::{last}:{length}::{local_index}")
            if A[end] != A[start]:
                start = 0
                if A[start] == A[end] and last == -1:
                    end = end
                else:
                    end = end-1 if last == -1 else last
                last = -1
                length = 0
            else:
                if length == 0:
                    local_index = (start, end)
                elif A[0] == A[end] and end > last:
                    last = end
                length += 1
                start += 1
                end -= 1
        print (f"{local_index}::{length}::{n}")
        if length > 0:
            end = local_index[1]
            return n - end
        else:
            return n if n%2 == 0 else n-1

if __name__ == "__main__":
    sol = Solution()
    print (sol.minCharsToMakePalindromic("ABDE"))
