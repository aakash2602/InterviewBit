class Solution():

    def strStr(self, A, B):
        n = len(B)
        m = len(A)
        if n == 0:
            return -1
        if m == 0:
            return -1
        length = 0
        last = -1
        index = 0
        i = 0
        start = -1
        while i < m:
            print (f"{i}:{A[i]}::{index}:{B[index]}::{length}:{last}::{start}")
            if A[i] == B[index]:
                if length == 0:
                    start = i
                if length > 0 and last == -1 and A[i] == B[0]:
                    last = i
                i += 1
                index += 1
                length += 1
                if index == n:
                    return start
            else:
                if A[i] == B[0] and last == -1:
                    i = i
                else:
                    i = last if last != -1 else i + 1
                index = 0
                length = 0
                last = -1
        return -1

if __name__ == "__main__":
    sol = Solution()
    print (sol.strStr("babbaaabaaaabbababaaabaabbbbabaaaabbabbabaaaababbabbbaaabbbaaabbbaabaabaaaaababbaaaaaabababbbbba", "bababbbbbbabbbaabbaaabbbaababa"))
