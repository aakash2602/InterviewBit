import collections
import sys

class Graph:

    def __init__(self, directed, vertices):
        self.graph = [[sys.maxsize if column != row else 0 for column in range(vertices)] for row in range(vertices)]
        self.directed = directed
        # print (self.graph)

    def graph_copy(self, graph):
        self.graph = graph
        # print (self.graph)

    def add_connection(self, a, b, c):
        if a == b:
            return
        if self.directed == True:
            self.graph[a][b] = c
        else:
            self.graph[a][b] = c
            self.graph[b][a] = c

    def get_min_index(self, distance, visited_vertex):
        min = sys.maxsize
        index = -1
        # print (distance)
        # print (visited_vertex)
        for i in range(len(distance)):
            if distance[i] < min and visited_vertex[i] == False:
                min = distance[i]
                index = i
        return index

    def dijkstra(self, start):
        visited_vertex = [False] * len(self.graph)
        distance = [sys.maxsize] * len(self.graph)
        distance[start] = 0

        for i in range(len(self.graph)):
            index = self.get_min_index(distance, visited_vertex)
            # print (index)
            visited_vertex[index] = True
            for j in range(len(self.graph)):
                # print (self.graph[index][j])
                if self.graph[index][j] < sys.maxsize and visited_vertex[j] == False:
                    # print ("inside 1")
                    # print (distance[index] + self.graph[index][j])
                    if distance[index] + self.graph[index][j] < distance[j]:
                        # print (self.graph[index][j])
                        distance[j] = distance[index] + self.graph[index][j]

        print (distance)
        # print (visited_vertex)

    def floyd_marshall(self):
        distance = self.graph
        for k in range(len(self.graph)):
            for i in range(len(self.graph)):
                for j in range(len(self.graph)):
                    distance[i][j] = min (distance[i][j], distance[i][k] + distance[k][j])
            print (distance)
        print (distance)

if __name__ == "__main__":
    g = Graph(False, 9)
    g.graph_copy([[0, 4, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 8, sys.maxsize],
           [4, 0, 8, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 11, sys.maxsize],
           [sys.maxsize, 8, 0, 7, sys.maxsize, 4, sys.maxsize, sys.maxsize, 2],
           [sys.maxsize, sys.maxsize, 7, 0, 9, 14, sys.maxsize, sys.maxsize, sys.maxsize],
           [sys.maxsize, sys.maxsize, sys.maxsize, 9, 0, 10, sys.maxsize, sys.maxsize, sys.maxsize],
           [sys.maxsize, sys.maxsize, 4, 14, 10, 0, 2, sys.maxsize, sys.maxsize],
           [sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 2, 0, 1, 6],
           [8, 11, sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize, 1, 0, 7],
           [sys.maxsize, sys.maxsize, 2, sys.maxsize, sys.maxsize, sys.maxsize, 6, 7, 0]
          ])
    g.dijkstra(0)
    g.floyd_marshall()