class Solution():

    def remove_duplicate(self, A):
        n = len(A)
        start = 2
        length = 2
        last = 2
        write = 0
        while start < n:
            print (f"{start}::{last}::{write}")
            if A[start] == A[start-1] and A[start-1] == A[start-2] and (not (last == start-1 and write == 1)):
                # A.pop(start)
                # n -= 1
                start += 1
                write = 0
            else:
                if A[last] != A[start]:
                    A[last] = A[start]
                    write = 1
                else:
                    write = 0
                start += 1
                length += 1
                last += 1
        A = A[:length]
        print (A)
        return length

if __name__ == "__main__":
    sol = Solution()
    print (sol.remove_duplicate([ 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3 ]))