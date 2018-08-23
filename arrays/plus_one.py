class Solution:
	# @param A : list of integers
	# @return a list of integers
	# def plusOne(self, A):
	#     num = 0
     #    number_of_element = len(A)
	#     A = reversed(A)
	#     for i in range(len(number_of_element)):
	#         num += A[i] * pow(10, i)
	#     num += 1
	#     B = []
	#     while num > 0:
	#         B.append(num % 10)
	#         num = num / 10
	#     return B
    def plusOne(self, A):
        if A:
            A[-1] += 1
            carry = int(A[-1]/10)
            for i in range(len(A) - 2, -1, -1):
                if carry == 1:
                    A[i] += 1
                    carry = int(A[i]/10)
                    A[i] = A[i] % 10
            if carry == 1:
                A.insert(0, 1)
            for i in range(len(A)):
                if A[i] > 0:
                    index = i
                    break
            return A[index:]
        else:
            return []


if __name__ == "__main__":
    sol = Solution()
    print (sol.plusOne([0, 1, 2, 3]))