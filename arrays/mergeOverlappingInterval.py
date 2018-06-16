class Solution():

    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        new_intervals = []
        new_intervals.append(intervals[0])
        for i in range(1, len(intervals)):
            start = new_intervals[-1][0]
            end = new_intervals[-1][1]
            if intervals[i][0] == start:
                new_intervals[-1][1] = max(end, intervals[i][1])
            elif intervals[i][0] <= end:
                new_intervals[-1][1] = max(end, intervals[i][1])
            else:
                new_intervals.append(intervals[i])
        return new_intervals



if __name__ == "__main__":
    sol = Solution()
    print (sol.merge([ (4, 100), (48, 94), (16, 21), (58, 71), (36, 53), (49, 68), (18, 42), (37, 90), (68, 75), (6, 57), (25, 78), (58, 79), (18, 29), (69, 94), (5, 31), (10, 87), (21, 35), (1, 32), (7, 24), (17, 85), (30, 95), (5, 63), (1, 17), (67, 100), (53, 55), (30, 63), (7, 76), (33, 51), (62, 68), (78, 83), (12, 24), (31, 73), (64, 74), (33, 40), (51, 63), (17, 31), (14, 29), (9, 15), (39, 70), (13, 67), (27, 100), (10, 71), (18, 47), (48, 79), (70, 73), (44, 59), (68, 78), (24, 67), (32, 70), (29, 94), (45, 90), (10, 76), (12, 28), (31, 78), (9, 44), (29, 83), (21, 35), (46, 93), (66, 83), (21, 72), (29, 37), (6, 11), (56, 87), (10, 26), (11, 12), (15, 88), (3, 13), (56, 70), (40, 73), (25, 62), (63, 73), (47, 74), (8, 36) ]))