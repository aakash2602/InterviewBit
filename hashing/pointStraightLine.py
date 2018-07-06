import fractions

class Solution():

    def points(self, A, B):
        hash_map = {}
        n = len(A)
        maxlen = 0
        if n == 1:
            return 1
        print (n)
        for i in range(n):
            for j in range(i+1, n):
                p1 = (A[i], B[i])
                p2 = (A[j], B[j])
                slope = 0.0
                if A[j] != A[i]:
                    if B[j] != B[i]:
                        slope = (p2[1] - p1[1]) / ((p2[0] - p1[0]) * 1.0)
                else:
                    slope = "inf"
                print (slope)
                if slope in hash_map:
                    # if i not in hash_map[slope]:
                    #     hash_map[slope].append(i)
                    # if j not in hash_map[slope]:
                    #     hash_map[slope].append(j)
                    hash_map[slope] += 1
                    if hash_map[slope] > maxlen:
                        maxlen = hash_map[slope]
                else:
                    hash_map[slope] = []
                    # hash_map[slope].append(i)
                    # hash_map[slope].append(j)
                    hash_map[slope] = 1
                    if hash_map[slope] > maxlen:
                        maxlen = hash_map[slope]
        return maxlen

    def maxPoints(self, A, B):
        hash_map = {}
        n = len(A)
        maxlen = 0
        if n == 1:
            return 1
        for i in range(n):
            for j in range(i + 1, n):
                p1 = (A[i], B[i])
                p2 = (A[j], B[j])
                if A[j] != A[i]:
                    yslope = p2[1] - p1[1]
                    xslope = p2[0] - p1[0]
                    slope = fractions._gcd(yslope, xslope)
                    yslope /= slope * 1.0
                    xslope /= slope * 1.0
                else:
                    xslope = "inf"
                    yslope = "inf"
                print (xslope, yslope)
                print (maxlen)
                # print (hash_map)
                if (xslope, yslope) in hash_map:
                    if i not in hash_map[(xslope, yslope)]:
                        hash_map[(xslope, yslope)].append(i)
                    if j not in hash_map[(xslope, yslope)]:
                        hash_map[(xslope, yslope)].append(j)
                    if len(hash_map[(xslope, yslope)]) > maxlen:
                        maxlen = len(hash_map[(xslope, yslope)])
                else:
                    hash_map[(xslope, yslope)] = []
                    hash_map[(xslope, yslope)].append(i)
                    hash_map[(xslope, yslope)].append(j)
                    if len(hash_map[(xslope, yslope)]) > maxlen:
                        maxlen = len(hash_map[(xslope, yslope)])
        print (hash_map)
        return maxlen

if __name__ == "__main__":
    sol = Solution()
    x = input()
    x = x.split()
    A = []
    B = []
    for i in range(int(x[0])):
        a = int(x[2*i + 1])
        b = int(x[2*i + 2])
        A.append(a)
        B.append(b)
    print (A)
    print (B)
    # print (sol.maxPoints([-6, 5, -18, 2, 5, -2], [-17, -16, -17, -4, -13, 20]))
    print (sol.points(A, B))

##  -6 -17 5 -16 -18 -17 2 -4 5 -13 -2 20
# 96 15 12 9 10 -16 3 -15 15 11 -10 -5 20 -3 -15 -11 -8 -8 -3 3 6 15 -14 -16 -18 -6 -8 14 9 -1 -7 -1 -2 3 11 6 20 10 -7 0 14 19 -18 -10 -15 -17 -1 8 7 20 -18 -4 -9 -9 16 10 14 -14 -15 -2 -10 -18 9 7 -5 -12 11 -17 -6 5 -17 -2 -20 15 -2 -5 -16 1 -20 19 -12 -14 -1 18 10 1 -20 -15 19 -18 13 13 -3 -16 -17 1 0 20 -18 7 19 1 -6 -7 -11 7 1 -15 12 -1 7 -3 -13 -11 2 -17 -5 -12 -14 15 -3 15 -11 7 3 19 7 -15 19 10 -14 -14 5 0 -1 -12 -4 4 18 7 -3 -5 -3 1 -11 1 -1 2 16 6 -6 -17 9 14 3 -13 8 -9 14 -5 -1 -18 -17 9 -10 19 19 16 7 3 7 -18 -12 -11 12 -15 20 -3 4 -18 1 13 17 -16 -15 -9 -9 15 8 19 -9 9 -17