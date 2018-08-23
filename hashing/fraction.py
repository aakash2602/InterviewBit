class Solution():

    def fractions(self, A, B):
        neg = '-' if (A < 0 and B > 0) or (A > 0 and B < 0) else ''
        A = abs(A)
        B = abs(B)
        num = int(A / B)
        num = str(num)
        rem = A % B
        index = 0
        frac = ''
        if A == 0:
            return "0"
        while rem != 0 and index < 1000:
            rem = rem * 10
            val = rem // B
            frac += str(val)
            rem = rem % B
            index += 1
        # print (frac)
        # print (num)
        n = len(frac)
        hash_map = {}
        val = ''
        start = 0
        last = n
        for i in range(n):
            number = frac[i]
            # print (number)
            if number not in hash_map:
                hash_map[number] = i
            else:
                pos = i - hash_map[number]
                val1 = frac[i:i+pos]
                val2 = frac[hash_map[number]:hash_map[number]+pos]
                print ("axa")
                print (pos)
                print (val1)
                print(val2)
                print (pos)
                print (i)
                if val1 == val2:
                    val = val1
                    start = hash_map[number]
                    last = i + pos
                    mode = 1
                    while last + pos < n:
                        new_val = frac[last:last+pos]
                        # print ("inside")
                        # print (new_val)
                        if new_val == val1:
                            last = last + pos
                            continue
                        else:
                            val = ''
                            last = last + pos
                            mode = 0
                            # break
                    if mode == 1:
                        last = n
                        break
                    # break
        if val != '':
            output = str(num) + '.' + frac[0:start] + "(" + val + ")" + frac[last:n]
        else:
            output = str(num) + '.' + frac[:32] if frac != '' else str(num)
        return neg + output

if __name__ == "__main__":
    sol = Solution()
    print (sol.fractions(353, 905))