class Solution():
    # @param A : list of integers
	# @return an integer
    def largestRectangleArea(self, A):
        rectangle_stack = []
        max_value = 0
        index = 0
        while index < len(A):
            if not rectangle_stack or A[index] >= A[rectangle_stack[-1]]:
                rectangle_stack.append(index)
                index += 1
            else:
                top = rectangle_stack[-1]
                rectangle_stack.pop(len(rectangle_stack) - 1)
                if not rectangle_stack:
                    length = index
                else:
                    length = index - rectangle_stack[-1] - 1
                area = A[top] * length
                if max_value < area:
                    max_value = area
        while rectangle_stack:
            top = rectangle_stack[-1]
            rectangle_stack.pop(len(rectangle_stack) - 1)

            if not rectangle_stack:
                length = index
            else:
                length = index - rectangle_stack[-1] - 1
            area = A[top] * length
            if max_value < area:
                max_value = area

        return max_value

    # def largestRectangleArea(self, A):
        # for i in range(len(A)):
        #     element = {}
        #     element['value'] = A[i]
        #     if rectangle_stack and rectangle_stack[-1]['value'] >= A[i]:
        #         for index, old_element in enumerate(rectangle_stack):
        #             if old_element['value'] >= A[i]:
        #                 element['start_index'] = old_element['start_index']
        #                 break
        #     else:
        #         element['start_index'] = i
        #     rectangle_stack.append(element)
        #
        #     popping_list = []
        #     for index, element in enumerate(rectangle_stack):
        #         if element['value'] > A[i]:
        #             rectangle_area = element['value'] * (i - element['start_index'])
        #             if max_value < rectangle_area:
        #                 max_value = rectangle_area
        #             popping_list.append(index)
        #     for index in reversed(popping_list):
        #         rectangle_stack.pop(index)
        #     print (rectangle_stack)
        #     print (max_value)
        # for index, element in enumerate(rectangle_stack):
        #     rectangle_area = element['value'] * (len(A) - element['start_index'])
        #     if max_value < rectangle_area:
        #         max_value = rectangle_area
        # return max_value

if __name__ == "__main__":
    sol = Solution()
    print (sol.largestRectangleArea([ 65, 19, 8, 39, 14, 21, 83, 87, 95, 11, 14, 58, 11, 90, 34, 96, 34, 62, 96, 38, 58, 57, 12, 78, 57, 60, 7, 58, 56, 49, 36, 67, 69, 30, 74, 46, 97, 62, 47, 42, 43, 98, 60, 32, 39, 75, 69, 28, 35, 52, 89, 78, 4, 26, 65, 21, 39, 89, 87, 69, 48, 60, 6, 21, 5, 98, 52, 59 ]))