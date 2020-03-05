from code.data_structures.graph.node import Node

class Graph(object):
  def __init__(self, nodes = []):
    self.nodes = nodes

  def search(self, value):
    for node in self.nodes:
      if node.value == value:
        return node
    return None

  def create_edge(self, u, v):
    u_node = self.search(u)
    v_node = self.search(v)

    if not u_node:
      u_node = Node(u, [])
      self.nodes.append(u_node)
    
    if not v_node:
      v_node = Node(v, [])
      self.nodes.append(v_node)
    
    u_node.adjacents.append(v_node) 

  def prettify(self):
    s = ''
    for node in self.nodes:
      s = s + 'Node: ' + str(node.value) + '\n'
      for n in node.adjacents:
        s = s + str(n.value)
      s = s + '\n'
    return s