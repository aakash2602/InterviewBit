class Interval():

    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution():

    def merge(self, intervals, new_interval):
        print(intervals)
        print(new_interval)
        new_intervals = []
        for i in range (len(intervals)):
            interval = Interval(intervals[i][0], intervals[i][1])
            new_intervals.append(interval)
        new_interval = Interval(new_interval[0], new_interval[1])
        intervals = new_intervals
        print (intervals)
        print (new_interval.start)

        if new_interval.start > new_interval.end:
            temp = new_interval.start
            new_interval.start = new_interval.end
            new_interval.end = temp
            print (new_interval.start)
            print(new_interval.end)

        mode = 0
        for i in range(len(intervals)):
            print(intervals[i].start)
            print(intervals[i].end)
            print (new_interval)
            print(new_interval.start)
            print(new_interval.end)
            if intervals[i].start > new_interval.end:
                intervals.insert(i, new_interval)
                print (1)
                mode = 1
                break
            elif intervals[i].start <= new_interval.start and intervals[i].end >= new_interval.start:
                intervals[i].start = min(intervals[i].start, new_interval.start)
                intervals[i].end = max(intervals[i].end, new_interval.end)
                print (2)
                mode = 1
                break
            elif intervals[i].start >= new_interval.start and intervals[i].end <= new_interval.end:
                intervals[i].start = min(intervals[i].start, new_interval.start)
                intervals[i].end = max(intervals[i].end, new_interval.end)
                print (3)
                mode = 1
                break
            elif intervals[i].start <= new_interval.start and intervals[i].end >= new_interval.end:
                intervals[i].start = min(intervals[i].start, new_interval.start)
                intervals[i].end = max(intervals[i].end, new_interval.end)
                print(4)
                mode = 1
                break
            elif intervals[i].start >= new_interval.start and intervals[i].start <= new_interval.end:
                intervals[i].start = min(intervals[i].start, new_interval.start)
                intervals[i].end = max(intervals[i].end, new_interval.end)
                print(5)
                mode = 1
                break
            # elif intervals[i].start == new_interval.start:
            #     intervals[i].end = max(intervals[i].end, new_interval.end)
            #     print (1)
            #     mode = 1
            #     break
            # elif intervals[i].end >= new_interval.start:
            #     intervals[i].end = max(intervals[i].end, new_interval.end)
            #     print(2)
            #     mode = 1
            #     break
            # elif intervals[i].start <= new_interval.end:
            #     intervals[i].start = min(new_interval.start, intervals[i].start)
            #     intervals[i].end = min(new_interval.end, intervals[i].end)
            #     print(4)
            #     mode = 1
            #     break
        if mode == 0:
            intervals.append(new_interval)
        new_list = intervals[:i + 1]
        for i in range(len(new_list)):
            print (f"{new_list[i].start} :: {new_list[i].end}")
        print (i)
        for j in range(i + 1, len(intervals)):
            start = new_list[-1].start
            end = new_list[-1].end
            if intervals[j].start == start:
                new_list[-1].end = max(end, intervals[j].end)
            elif intervals[j].start <= end:
                new_list[-1].end = max(end, intervals[j].end)
            else:
                new_list.append(intervals[j])
        for i in range(len(new_list)):
            print (f"{new_list[i].start} :: {new_list[i].end}")
        return new_list



if __name__ == "__main__":
    sol = Solution()
    print (sol.merge([ (31935139, 38366404), (54099301, 76986474), (87248431, 94675146) ], (43262807, 68844111)))