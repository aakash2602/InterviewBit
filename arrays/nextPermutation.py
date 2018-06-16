class Solution():

    def nextPermutation(self, A):
        last_value = A[-1]
        for i in range(len(A) - 2, -1, -1):
            print (last_value)
            print (A[i])
            if A[i] < last_value:
                for j in range(len(A) - 1, i, -1):
                    if A[j] > A[i]:
                        temp = A[i]
                        A[i] = A[j]
                        A[j] = temp
                        print (A)
                        print (A[j])
                        A[i+1:] = list(reversed(A[i+1:]))
                        return A
            last_value = A[i]
        return list(reversed(A))


if __name__ == "__main__":
    sol = Solution()
    print (sol.nextPermutation([ 626, 436, 819, 100, 382, 173, 817, 581, 220, 95, 814, 660, 397, 852, 15, 532, 564, 715, 179, 872, 236, 790, 223, 379, 83, 924, 454, 846, 742, 730, 689, 112, 110, 516, 85, 149, 228, 202, 988, 212, 69, 602, 887, 445, 327, 527, 347, 906, 54, 460, 517, 376, 395, 494, 827, 448, 919, 799, 133, 879, 709, 184, 812, 514, 976, 700, 156, 568, 453, 267, 547, 8, 951, 326, 652, 772, 213, 714, 706, 972, 318, 768, 506, 59, 854, 422 ]))