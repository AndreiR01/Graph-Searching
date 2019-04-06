from heapq import heappop, heappush
from math import inf

graph = {
        'A': [('B', 10), ('C', 3)],     #vertex A is connected to vertex B      with a weight of 10 and to vertex C with a weight of 3
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [('A', 7)],
        'B': [('C', 3), ('D', 2)]
    }

def dijkstras(graph, start):               #start refers to the start vertrex
    distances = {}                         #instantiate a distances dictionary
    #distances dictionary will map verticies to their distance from their start vertex
    for vertex in graph:                   #loops over keys in graph
        distances[vertex] = inf            #sets all vertices to infinity.

    distances[start] = 0                   #sets the start  vertex to 0
    vertices_to_explore = [(0, start)]     #initialises a heap node with following tuple inside

    #we will transverse the vertices_to_explore heap until it is empty. We will pop off the vertex with the minimum distance from start. Below in our while loop, we will iterate ovefr the neighbouring vertices of current_vertex and add each neighbor(and its distance from start) to the vertices_to_explore min-heap.

    while vertices_to_explore:
        #heappop -> removes and returns the smallest value from the heap
        #heappush -> will add a value to the heap and ajust the heap
        #current_distance -> refers to the weight value
        #current_vertex -> refers to the vertexs
        current_distance, current_vertex = heappop(vertices_to_explore) #we remove the smallest value in the heap and assigns its weight to current_distance and current_vertex to its vertex value

        #The above syntax can be replicated as such(less effective):
        # current_distance = heappop(vertices_to_explore)[0]
        # current_vertex = heappop(vertices_to_explore)[1]
        # print(current_distance)
        # print(current_vertex)


        for neighbor, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance
                #push a tuple of (new_distance, neighbor) onto vertices_to_explore
                heappush(vertices_to_explore, (new_distance, neighbor))

    return distances

distances_from_a = dijkstras(graph, 'A')

print("\n\nShortest Distances: {0}".format(distances_from_a))
