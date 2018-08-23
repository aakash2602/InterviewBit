class Solution():

    def count_and_say(self, n):
        seq = '1'
        count = 1
        while count < n:
            next_seq = ''
            last = ''
            s = len(seq)
            char_count = 0
            for i in range(s):
                if last != seq[i]:
                    if char_count > 0:
                        next_seq += str(char_count) + last
                    last = seq[i]
                    char_count = 1
                else:
                    char_count += 1
            if char_count > 0:
                next_seq += str(char_count) + last
            seq = next_seq
            count += 1
        return seq

if __name__ == "__main__":
    sol = Solution()
    print (sol.count_and_say(20))