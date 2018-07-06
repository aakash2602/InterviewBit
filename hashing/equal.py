class Solution():

    def equal(self, A):
        hash_map = {}
        n = len(A)
        last_values = []
        for i in range(n):
            mode = 0
            for j in range(i+1, n):
                val = A[i] + A[j]
                # print (val)
                values= []
                if val in hash_map:
                    if i not in hash_map[val] and j not in hash_map[val]:
                        values.extend(hash_map[val])
                        values.append(i)
                        values.append(j)
                        # values.sort()
                        print ("Values")
                        print (values)
                        print (last_values)
                        # mode = 1
                        if not last_values:
                            last_values = values.copy()
                        else:
                            if last_values > values:
                                last_values = values.copy()
                                # last_values.sort()
                        # break
                else:
                    hash_map[val] = []
                    hash_map[val].append(i)
                    hash_map[val].append(j)
            # if mode == 1:
            #     break
        #     print (hash_map)
        # print (val)
        # last_values.sort()
        return last_values

if __name__ == "__main__":
    sol = Solution()
    print (sol.equal([1, 2, 3, 4]))
    # print (sol.equal([3, 4, 7, 1, 2, 9, 8]))