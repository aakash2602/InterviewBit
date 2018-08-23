class Solution():

    def anagrams(self, A):
        n = len(A)
        hash_map = {}
        for i in range(n):
            val = [letter for letter in A[i]]
            val.sort()
            val = ''.join(val)
            if val in hash_map:
                hash_map[val].append(i+1)
            else:
                hash_map[val] = [i+1]

        out = []
        # print (hash_map)
        for i in range(n):
            val = [letter for letter in A[i]]
            val.sort()
            val = ''.join(val)
            length = len(hash_map[val])
            if length > 1:
                out.append(hash_map[val])
                hash_map[val] = []
            elif length == 1:
                out.append(hash_map[val])
                hash_map[val] = []
        # print(hash_map)
        return out

if __name__ == "__main__":
    sol = Solution()
    print (sol.anagrams([ "abbbaabbbabbbbabababbbbbbbaabaaabbaaababbabbabbaababbbaaabbabaabbaabbabbbbbababbbababbbbaabababba", "abaaabbbabaaabbbbabaabbabaaaababbbbabbbaaaabaababbbbaaaabbbaaaabaabbaaabbaabaaabbabbaaaababbabbaa", "babbabbaaabbbbabaaaabaabaabbbabaabaaabbbbbbabbabababbbabaabaabbaabaabaabbaabbbabaabbbabaaaabbbbab", "bbbabaaabaaaaabaabaaaaaaabbabaaaabbababbabbabbaabbabaaabaabbbabbaabaabaabaaaabbabbabaaababbaababb", "abbbbbbbbbbbbabaabbbbabababaabaabbbababbabbabaaaabaabbabbaaabbaaaabbaabbbbbaaaabaaaaababababaabab", "aabbbbaaabbaabbbbabbbbbaabbababbbbababbbabaabbbbbbababaaaabbbabaabbbbabbbababbbaaabbabaaaabaaaaba", "abbaaababbbabbbbabababbbababbbaaaaabbbbbbaaaabbaaabbbbbbabbabbabbaabbbbaabaabbababbbaabbbaababbaa", "aabaaabaaaaaabbbbaabbabaaaabbaababaaabbabbaaaaababaaabaabbbabbababaabababbaabaababbaabbabbbaaabbb" ]))
    print (sol.anagrams(["cat", "dog", "god", "tca"]))