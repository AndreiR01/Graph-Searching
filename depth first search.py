def dfs(graph, current_vertex, target_value, visited=None):
    if visited == None:
        return []
    visited.append(current_vertex)

    #Base case
    if current_vertex is target_value:
        return visited

    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, target_value, visited)

            if path:
                return path

the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }


print(dfs(the_most_dangerous_graph, "crocodiles", "bees"))
