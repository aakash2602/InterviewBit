class Solution():

    def longestPalindrome(self, A):
        index = (-1. -1)
        n = len(A)
        max_length = -1
        for i in range(n):
            start = i
            end = n - 1
            length = 0
            local_index = (i, end)
            last = -1
            while end >= start:
                print (f"{start}:{A[start]}::{end}:{A[end]}::{length}::{local_index}::{last}")
                if A[start] != A[end]:
                    start = i
                    if A[start] == A[end] and last == -1:
                        end = end
                    else:
                        end = end - 1 if last == -1 else last
                    length = 0
                    last = -1
                else:
                    if length == 0:
                        local_index = (i, end)
                    elif A[i] == A[end] and end > last:
                        last = end
                    length += 1
                    start += 1
                    end -= 1
                # print(f"{start}:{A[start]}::{end}:{A[end]}::{length}::{local_index}::{last}")
            if length > 0:
                if max_length < local_index[1] - local_index[0] + 1:
                    index = (local_index[0], local_index[1])
                    max_length = local_index[1] - local_index[0] + 1
                    print(f"{index}::{max_length}")
        if max_length == -1:
            return ""
        else:
            return A[index[0]:index[1]+1]

if __name__ == "__main__":
    sol = Solution()
    print (sol.longestPalindrome("aabaaa"))

    # caccbcbaabacabaccacaaccaccaaccbbcbcbbaacabccbcccbbacbbacbccaccaacaccbbcc
    # abbcccbbbcaaccbababcbcabca
