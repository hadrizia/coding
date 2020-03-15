'''
  Problem resume: Given a list of projects and a list of dependencies, find a build order that allow the projects to be built. 
  If there's not a valid build order, return an error.
'''
from code.data_structures.graph.graph import Graph
from code.data_structures.stack.stack import Stack
from code.data_structures.graph.node import Node

from collections import defaultdict

def build_graph(projects, dependencies):
  dict = defaultdict(list)
  for p, d in dependencies:
    dict[p].append(d)

  graph = Graph(nodes = [])

  for p in projects:
    node = Node(p, [])
    graph.nodes.append(node)

  for u in dict:
    for v in dict[u]:
      graph.create_edge(u, v)
  return graph

def build_stack(graph):
  stack = Stack()
  for v in graph.nodes:
    if v.color == 'white': # not processed yet
      if not dfs(v, stack): # if not found a valid build order
        return None
  return stack

def dfs(v, stack):
  if v.color == 'gray':
    return False # Found a cycle
  
  if v.color == 'white':
    v.color = 'gray'
    for u in v.adjacents:
      if not dfs(u, stack):
        return False # End the function

    v.color = 'black' # v is processed
    stack.push(v)
  return True

def build_order(projects, dependencies):
  graph = build_graph(projects, dependencies)
  stack = build_stack(graph)
  if stack:
    order = []
    while not stack.is_empty():
      order.append(stack.pop().data.value)
    return order
  else:
    raise Exception("Could not found a valid build order :(")

def tests():
  projects = ['a', 'b', 'c', 'd', 'e', 'f']
  dependencies = [
    ('a', 'd'),
    ('f', 'b'),
    ('b', 'd'),
    ('f', 'a'),
    ('d', 'c')
  ]

  build_order_expected_list = ['f', 'e', 'b', 'a', 'd', 'c']
  assert build_order(projects, dependencies) == build_order_expected_list

  projects2 = ['a', 'b', 'c']
  dependencies2 = [
    ('a', 'b'),
    ('b', 'c'),
    ('c', 'a')
  ]

  try:
    build_order(projects2, dependencies2)
  except Exception as e:
    assert str(e) == 'Could not found a valid build order :('

if __name__ == "__main__":
  tests()