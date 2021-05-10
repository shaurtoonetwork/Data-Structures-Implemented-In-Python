graph = {
  0 : [1,2],
  1 : [2],
  2 : [0,3],
  3 : [3]
}

visited = [] 
q = []   

def bfs(visited, graph, node):
  visited.append(node)
  q.append(node)
  print("The Following is BFS Traversal, starting from :", node)
  while q:
    s = q.pop(0)
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        q.append(neighbour)

bfs(visited, graph, 3)