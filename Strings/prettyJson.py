class Solution():

    def prettyJson(self, A):
        n = len (A)
        count = 0
        out = []
        line = ''
        i = 0
        while i < n:
            if A[i] == '{' or A[i] == '[':
                if line != '':
                    out.append(line)
                line = '\t' * count + A[i]
                out.append(line)
                count += 1
                line = ''
            elif A[i] == '}' or A[i] == ']':
                if line != '':
                    out.append(line)
                count -= 1
                if i+1 < n and A[i+1] == ',':
                    line = '\t' * count + A[i:i+2]
                    i += 1
                else:
                    line = '\t' * count + A[i]
                out.append(line)
                line = ''
            elif A[i] == ' ':
                continue
            elif A[i] == ',':
                line += A[i]
                out.append(line)
                line = ''
            else:
                line = '\t' * count if line == '' else line
                line += A[i]
            i += 1
        return out

if __name__ == "__main__":
    sol = Solution()
    print (sol.prettyJson('{"attributes":[{"nm":"ACCOUNT","lv":[{"v":{"Id":null,"State":null},"vt":"java.util.Map","cn":1}],"vt":"java.util.Map","status":"SUCCESS","lmd":13585},{"nm":"PROFILE","lv":[{"v":{"Party":null,"Ads":null},"vt":"java.util.Map","cn":2}],"vt":"java.util.Map","status":"SUCCESS","lmd":41962}]}'))