class Solution():

    def validAddress(self, A):
        if len(A) > 12:
            return []
        output = []
        ## first value
        first = self.get_possible_option(A, 1)
        print (first)
        second = []
        for element in first:
            print (element)
            sec = self.get_possible_option(A[len(element):], 2)
            print (sec)
            if len(sec) == 0:
                # first.remove(element)
                continue
            second.extend(sec)
        third = []
        for element in second:
            print (element)
            sec = self.get_possible_option(A[len(element):], 2)
            print (sec)
            if len(sec) == 0:
                # first.remove(element)
                continue
            third.extend(sec)
        print (first)
        print (second)
        print (third)

    def get_possible_option(self, A, pos):
        options = []
        length = len(A)
        if A[0] == '0':
            options.append('0')
        elif int(A[0]) > 2:
            if length >= (4 - pos + 1) and length <= (4 - pos)*3 + 1:
                options.append((A[0]))
            if length >= ((4 - pos + 2)) and length <= (4 - pos)*3 + 2:
                options.append((A[0:2]))
        else:
            if length >= (4 - pos + 1) and length <= (4 - pos)*3 + 1:
                options.append((A[0]))
            if length >= ((4 - pos + 2)) and length <= (4 - pos)*3 + 2:
                options.append((A[0:2]))
            if length >= ((4 - pos + 3)) and length <= (4 - pos)*3 + 3:
                options.append((A[0:3]))
        return options

    def is_valid(self, ip):

        # Spliting by "."
        ip = ip.split(".")

        # Checking for the corner cases
        for i in ip:
            if len(i) > 3 or int(i) < 0 or int(i) > 255:
                return False
            if len(i) > 1 and int(i) == 0:
                return False
            if len(i) > 1 and int(i) != 0 and i[0] == '0':
                return False
        return True

    # Function converts string to IP address
    def convert(self, A):
        sz = len(A)

        # Check for string size
        if sz > 12:
            return []
        snew = A
        l = []

        # Generating different combinations.
        for i in range(1, sz - 2):
            for j in range(i + 1, sz - 1):
                for k in range(j + 1, sz):
                    snew = snew[:k] + "." + snew[k:]
                    snew = snew[:j] + "." + snew[j:]
                    snew = snew[:i] + "." + snew[i:]

                    print (snew)
                    # Check for the validity of combination
                    if self.is_valid(snew):
                        l.append(snew)
                    snew = A
        return l

if __name__ == "__main__":
    sol = Solution()
    print (sol.convert("0100100"))
