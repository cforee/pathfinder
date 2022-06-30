import csv
from tkinter import *
from src.node import Node
import src.constants as constants
import time

class Map:
  nodes = []
  path = []
  start_node = None
  end_node = None
  canvas_width = None
  canvas_height = None

  def __init__(self, filename):
    self.nodes = self._build_nodes(filename)
    self._init_canvas(self.nodes)
    self.draw()
    path = self._find_path(self.start_node, self.end_node)
    self.canvas.pack()

    for node in path[1:-1]:
      node.walk()
      self.root_window.update()
      time.sleep(0)
    self.root_window.mainloop()

  def draw(self):
    for node in self.nodes:
      node.draw(self.canvas)


  #
  # Private
  #
 
  def _find_path(self, start_node, end_node):
    open_nodes = []
    closed_nodes = []
    open_nodes.append(start_node)

    print('Finding path from node id: {} to node id: {}'.format(start_node.id, end_node.id))
    while len(open_nodes) > 0:
      current_node = open_nodes.pop(0)
      closed_nodes.append(current_node)

      if current_node == end_node:
        # Base case: We've found the end node!
        # Break while loop and return the path
        return self._build_path(current_node)

      for neighbor in current_node.neighbors(self.nodes):
        if neighbor in closed_nodes or not neighbor.is_walkable:
          continue

        if neighbor not in open_nodes or neighbor.f_cost > current_node.f_cost:
          neighbor.parent = current_node
          neighbor.f_cost = current_node.f_cost + self._calculate_cost(current_node, neighbor)
          if neighbor not in open_nodes:
            open_nodes.append(neighbor)
          open_nodes.append(neighbor)
    return []

  def _calculate_cost(self, node1, node2):
    return node1.distance_to(node2)

  def _build_path(self, node):
    path = []
    while node.parent:
      path.append(node)
      node = node.parent
    path.append(node)
    path.reverse()
    return path

  def _build_nodes(self, filename):
    nodes = []
    nodemap = self._read_nodemap_file(filename)
    for x, row in enumerate(nodemap):
      nodes_row = []
      for y, col in enumerate(row):
        config = constants.NODE_TYPES[col.strip()]
        node = Node(x + 1, y + 1, config)
        nodes_row.append(node)
        if node.is_start:
          self.start_node = node
        if node.is_end:
          self.end_node = node
      nodes.append(nodes_row)
    self.canvas_width = constants.NODE_PIXEL_SIZE * (len(nodes[0]) + 1) - 2
    self.canvas_height = constants.NODE_PIXEL_SIZE * (len(nodes) + 1) - 2

    # flatten the list of lists into a single list
    return [node for row in nodes for node in row]

  def _read_nodemap_file(self, filename):
    filepath = './res/nodemaps/{}'.format(filename)
    with open(filepath) as f:
      reader = csv.reader(f)
      nodemap = list(reader)
    return nodemap

  def _init_canvas(self, nodes):
    self.root_window = Tk()
    self.root_window.title(constants.APP_TITLE)
    self.root_window.geometry(self._root_window_geometry)
    self.canvas = Canvas(self.root_window, width=self.canvas_width, height=self.canvas_height)

  @property
  def _root_window_geometry(self):
    w = self.canvas_width
    h = self.canvas_height
    return '{}x{}'.format(w + int(w/5), h + int(h/5))
