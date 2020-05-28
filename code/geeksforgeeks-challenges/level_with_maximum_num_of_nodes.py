from collections import defaultdict

def level_with_max_nodes(graph, visited, node, dict_levels = defaultdict(int), current_level = 0):
  if node not in visited:
    visited.add(node)
    dict_levels[current_level] += 1
  for n in graph[node]:
    level_with_max_nodes(graph, visited, n, dict_levels, current_level + 1)
    
  else:
    level_max_nodes = sorted(dict_levels.items(), key=lambda v: v[1], reverse=True)[0]
    return level_max_nodes[0]

def tests():
  graph = {
    1: [4, 6],
    2: [1, 3],
    3: [8],
    4: [],
    5: [],
    6: [5],
    8: []
  }
  
  visited = set()
  root = 2
 
  assert level_with_max_nodes(graph, visited, root) == 2

if __name__ == "__main__":
  tests()