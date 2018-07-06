import heapq

class Solution():

    def distinct(self, A, B):
        heap = []
        if B > len(A):
            return []
        out = []
        index = 0
        n = len(A)
        for i in range(n - B + 1):
            while index < i + B:
                mode = 0
                m = len(heap)
                for j in range(m):
                    if heap[j][1] == A[index]:
                        heap[j] = (index, A[index])
                        heapq.heapify(heap)
                        mode = 1
                        break
                if mode == 0:
                    heapq.heappush(heap, (index, A[index]))
                index += 1
            out.append(len(heap))
            # print(heap)
            if heap[0][0] == i:
                val = heapq.heappop(heap)
                # print (val)
        return out

    def distinctNum(self, A, B):
        hash_map = {}
        if B > len(A):
            return []
        out = []
        index = 0
        n = len(A)
        count = 0
        for i in range(n - B + 1):
            while index < i + B:
                if A[index] not in hash_map or hash_map[A[index]] == 0:
                    hash_map[A[index]] = 1
                    count += 1
                else:
                    hash_map[A[index]] += 1
                index += 1
            out.append(count)
            hash_map[A[i]] -= 1
            if hash_map[A[i]] == 0:
                count -= 1
        return out

if __name__ == "__main__":
    sol = Solution()
    print (sol.distinct([1, 1, 1, 1, 1, 1], 3))
    # print(sol.distinctNum([1, 1, 1, 1, 1, 1], 3))