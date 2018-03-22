import collections


class Graph:

    def __init__(self, directed):
        self.graph = collections.defaultdict(set)
        self.directed = directed
        # print (self.graph)

    def add_connection(self, a, b):
        if self.directed == True:
            self.graph[a].add(b)
        else:
            self.graph[a].add(b)
            self.graph[b].add(a)

    def bfs_traversal(self, start):
        if start not in self.graph:
            return "Node not in Graph"
        queue = collections.deque()
        queue.append(start)
        visited_vertex = collections.defaultdict(None)
        output = ''
        while len(queue) != 0:
            vertex = queue.popleft()
            # print (vertex)
            output = output + ' ' + str(vertex)
            visited_vertex[vertex] = 1
            for connected_vertex in self.graph[vertex]:
                if connected_vertex not in visited_vertex:
                    queue.append(connected_vertex)
            # print (queue)
        del visited_vertex
        del queue
        return output.strip()


    def dfs_traversal(self, start):
        visited_vertex = collections.defaultdict(None)
        output = self.dfs(start, visited_vertex, '')
        del visited_vertex
        return output.strip()

    def dfs(self, start, visited_vertex, output):
        print ("inside dfs: " + str(start))
        visited_vertex[start] = 1
        output = output + ' ' + str(start)
        for connected_vertex in self.graph[start]:
            if connected_vertex not in visited_vertex:
                output = self.dfs(connected_vertex, visited_vertex, output)
        return output


if __name__ == "__main__":
    g = Graph(False)
    g.add_connection(2, 0)
    g.add_connection(0, 1)
    g.add_connection(1, 1)
    g.add_connection(2, 3)
    g.add_connection(3, 3)
    g.add_connection(1, 2)
    # output = g.bfs_traversal(2)
    output = g.dfs_traversal(2)
    print (output)
