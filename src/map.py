import csv
from tkinter import *
from src.node import Node
import src.constants as constants

class Map:
  nodes = []
  start_node = None
  end_node = None

  def __init__(self, filename):
    self.nodes = self._build_nodes(filename)
    self._init_canvas(self.nodes)

  def draw(self):
    self.canvas.pack()
    for row in self.nodes:
      for node in row:
        node.draw(self.canvas)
    self.root_window.mainloop()


  #
  # Private
  #
 
  def _build_nodes(self, filename):
    nodes = []
    nodemap = self._read_nodemap_file(filename)
    for x, row in enumerate(nodemap):
      nodes_row = []
      for y, col in enumerate(row):
        config = constants.NODE_TYPES[col.strip()]
        node = Node(x + 1, y + 1, config)
        nodes_row.append(node)
        if node.is_origin:
          self.start_node = node
        if node.is_target:
          self.end_node = node
      nodes.append(nodes_row)
    return nodes

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
    self.canvas = Canvas(self.root_window, width=self._canvas_width, height=self._canvas_height)

  @property
  def _canvas_width(self):
    return constants.NODE_PIXEL_SIZE * (len(self.nodes[0]) + 1) - 2

  @property
  def _canvas_height(self):
    return constants.NODE_PIXEL_SIZE * (len(self.nodes) + 1) - 2

  @property
  def _root_window_geometry(self):
    w = self._canvas_width
    h = self._canvas_height
    return '{}x{}'.format(w + int(w/5), h + int(h/5))
