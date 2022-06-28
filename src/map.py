import csv
from tkinter import *
from src.node import Node
import src.constants as constants

class Map:
  node_pixel_size = constants.NODE_PIXEL_SIZE

  def __init__(self, filename):
    self.init_nodemap(filename)
    self.init_canvas()

  def init_nodemap(self, filename):
    self.nodes = []
    filepath = './res/nodemaps/{}'.format(filename)
    with open(filepath) as f:
      reader = csv.reader(f)
      nodemap = list(reader)
    for x, row in enumerate(nodemap):
      nodes_row = []
      for y, col in enumerate(row):
        config = constants.NODE_TYPES[col.strip()]
        node = Node(x + 1, y + 1, self.node_pixel_size, config)
        nodes_row.append(node)
      self.nodes.append(nodes_row)

  def init_canvas(self):
    self.root_window = Tk()
    self.root_window.title('Pathfinder Beta')
    self.root_window.geometry('640x640')
    width = self.node_pixel_size * (len(self.nodes[0]) + 1) - 2
    height = self.node_pixel_size * (len(self.nodes) + 1) - 2
    self.canvas = Canvas(self.root_window, width=width, height=height)

  def draw(self):
    self.canvas.pack()
    for row in self.nodes:
      for node in row:
        node.draw(self.canvas)

    self.root_window.mainloop()
