class Solution():

    def maxSet(self, A):
        max_sum = 0
        last_sum = 0
        max_list = []
        last_list = []
        for i in range(len(A)):
            if A[i] < 0:
                if last_sum > max_sum:
                    max_sum = last_sum
                    max_list = last_list
                    last_sum = 0
                    last_list = []
                elif last_sum == max_sum:
                    max_list = last_list if len(last_list) > len(max_list) else max_list
                    last_sum = 0
                    last_list = []
                else:
                    last_sum = 0
                    last_list = []
            else:
                last_list.append(A[i])
                last_sum += A[i]
        if last_sum > max_sum:
            max_list = last_list
        elif last_sum == max_sum:
            max_list = last_list if len(last_list) > len(max_list) else max_list
        return max_list

if __name__ == "__main__":
    sol = Solution()
    print (sol.maxSet([ 24115, -75629, -46517, 30105, 19451, -82188, 99505, 6752, -36716, 54438, -51501, 83871, 11137, -53177, 22294, -21609, -59745, 53635, -98142, 27968, -260, 41594, 16395, 19113, 71006, -97942, 42082, -30767, 85695, -73671 ]))