import heapq

h = []
heapq.heappush(h, (100, 6, 6))
heapq.heappush(h, (10000, 0, 0))
heapq.heappush(h, (1000, 5, 5))
heapq.heappush(h, (10, 6, 6))
heapq.heappush(h, (1, 8, 6))
a = [heapq.heappop(h) for i in range(len(h))]
print (a)