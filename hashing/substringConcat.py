class Solution():

    def substring(self, A, B):
        n = len(A)
        m = len(B)
        if m == 0:
            return []
        word_len = 0
        hash_map = {}
        for i in range(m):
            if B[i] in hash_map:
                hash_map[B[i]] += 1
            else:
                hash_map[B[i]] = 1
            word_len = len(B[i])

        out = []
        for i in range(n):
            allsubs = 1
            map_int = hash_map.copy()
            for j in range(m):
                word = A[i + j*word_len:i + (j+1)*word_len]
                if word not in map_int:
                    allsubs = 0
                    break
                else:
                    if map_int[word] == 0:
                        allsubs = 0
                        break
                    else:
                        map_int[word] -= 1
            if allsubs == 1:
                out.append(i)

        return out

if __name__ == "__main__":
    sol = Solution()
    print (sol.substring("barfoothefoobarman", ["foo", "bar"]))
    # print (sol.substring("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", [ "aaa", "aaa", "aaa", "aaa", "aaa" ]))