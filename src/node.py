import math

class Node:
  def __init__(self, node_x, node_y, pixel_size):
    self.x = node_x
    self.y = node_y
    self.pixel_size = pixel_size
    self.pixel_dims = {
      'top': self.y * self.pixel_size,
      'right': self.x * pixel_size + self.pixel_size,
      'bottom': self.y * pixel_size + self.pixel_size,
      'left': self.x * self.pixel_size
    }

