class Solution():

    def merge(self, A, B):
        pointer1 = 0
        pointer2 = 0
        while pointer1 < len(A) or pointer2 < len(B):
            if pointer1 == len(A):
                A.extend(B[pointer2:])
                break
            elif pointer2 == len(B):
                break
            elif A[pointer1] <= B[pointer2]:
                pointer1 += 1
            elif A[pointer1] > B[pointer2]:
                A.insert(pointer1, B[pointer2])
                pointer1 += 1
                pointer2 += 1
        # return A
        output = ''
        for i in range(len(A)):
            output += str(A[i]) + ' '
        print (output)

if __name__ == "__main__":
    sol = Solution()
    print (sol.merge([ -4, 3 ], [ -2, -2 ]))