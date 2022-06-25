import csv
from tkinter import *
from src.node import Node

class Map:
  node_pixel_size = 67

  def __init__(self, filename):
    self.init_canvas()
    self.init_nodemap(filename)

  def init_nodemap(self, filename):
    self.nodes = []
    filepath = './res/nodemaps/{}'.format(filename)
    with open(filepath) as f:
      reader = csv.reader(f)
      nodemap = list(reader)
    for y, row in enumerate(nodemap):
      nodes_row = []
      for x, col in enumerate(row):
        node = Node(x, y, self.node_pixel_size)
        nodes_row.append(node)
      self.nodes.append(nodes_row)

  def init_canvas(self):
    self.root_window = Tk()
    self.root_window.title('Pathfinder Beta')
    self.root_window.geometry('603x603')
    self.canvas = Canvas(self.root_window, width=603, height=603)

  def draw(self):
    for y, row in enumerate(self.nodes):
      for x, node in enumerate(row):
        self.canvas.create_rectangle(
          node.pixel_dims['top'],
          node.pixel_dims['left'],
          node.pixel_dims['bottom'],
          node.pixel_dims['right']
        )
    self.canvas.pack()
    self.root_window.mainloop()

