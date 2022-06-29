import src.constants as constants
import math

class Node:
  NODE_PIXEL_SIZE = constants.NODE_PIXEL_SIZE

  canvas = None
  parent = None
  is_visited = False

  def __init__(self, node_x, node_y, config):
    self.id = '{}_{}'.format(node_x, node_y)
    self.x = node_x
    self.y = node_y
    self.config = config
    self.color = config['color']
    self.type = config['type']
    self.is_walkable = config['walkable']
    self.is_start = config['type'] == 'start'
    self.is_end = config['type'] == 'end'
    self.f_cost = math.inf

    self.pixel_dims = {
      'top': self.y * self.NODE_PIXEL_SIZE,
      'right': self.x * self.NODE_PIXEL_SIZE + self.NODE_PIXEL_SIZE,
      'bottom': self.y * self.NODE_PIXEL_SIZE + self.NODE_PIXEL_SIZE,
      'left': self.x * self.NODE_PIXEL_SIZE
    }

  def draw(self, canvas):
    self.canvas = canvas
    self._redraw()

  def walk(self):
    self.color = constants.COLORS['path']
    self._redraw()

  def neighbors(self, nodes):
    neighbors = []
    for node in nodes:
      if node.is_walkable and node.id != self.id and self._is_neighbor(node):
        neighbors.append(node)
    return neighbors

  def distance_to(self, node):
    return abs(self.x - node.x) + abs(self.y - node.y)


  #
  # Private
  #

  def _is_neighbor(self, node):
    if self.x == node.x and abs(self.y - node.y) == 1:
      return True
    if self.y == node.y and abs(self.x - node.x) == 1:
      return True
    return False

  def _redraw(self):
    self.canvas.create_rectangle(
      self.pixel_dims['top'],
      self.pixel_dims['left'],
      self.pixel_dims['bottom'],
      self.pixel_dims['right'],
      fill=self.color
    )
    #self.canvas.create_text((self.pixel_dims['top'] + 21, self.pixel_dims['left'] + 12), text=self.id)
