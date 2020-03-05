from code.data_structures.graph.graph import Graph
from code.data_structures.graph.node import Node
from code.data_structures.queue.queue import Queue

def generate_graph(dict):
  g = Graph()
  for k in dict:
    for v in dict[k]:
      g.create_edge(k, v)
  return g

def search_path(graph, s, d):
  if s == d:
    return True

  marked = [False for _ in range(len(graph.nodes))]

  q = Queue()
  marked[s.value - 1] = True
  q.enqueue(s)

  while not q.is_empty():
    node = q.dequeue().data
    for neighbor in node.adjacents:
      if not marked[neighbor.value - 1]:
        if neighbor == d:
          return True
        else:
          marked[neighbor.value - 1] = True
          q.enqueue(neighbor)
  return False

def tests():
  dict = {
    1: [4],
    2: [3],
    3: [1]
  }

  graph = generate_graph(dict)

  node_1 = graph.search(1)
  node_2 = graph.search(2)
  node_3 = graph.search(3)
  node_4 = graph.search(4)

  assert search_path(graph, node_1, node_2) == False
  assert search_path(graph, node_1, node_3) == False
  assert search_path(graph, node_2, node_1) == True

if __name__ == "__main__":
  tests()