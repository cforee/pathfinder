import src.constants as constants
import math

class Node:
  node_pixel_size = constants.NODE_PIXEL_SIZE

  def __init__(self, node_x, node_y, config):
    self.id = '{}_{}'.format(node_x, node_y)
    self.x = node_x
    self.y = node_y
    self.color = config['color']
    self.type = config['type']
    self.walkable = config['walkable']
    self.is_origin = config['type'] == 'origin'
    self.is_target = config['type'] == 'target'

    self.pixel_dims = {
      'top': self.y * self.node_pixel_size,
      'right': self.x * self.node_pixel_size + self.node_pixel_size,
      'bottom': self.y * self.node_pixel_size + self.node_pixel_size,
      'left': self.x * self.node_pixel_size
    }

  def draw(self, canvas):
    canvas.create_rectangle(
      self.pixel_dims['top'],
      self.pixel_dims['left'],
      self.pixel_dims['bottom'],
      self.pixel_dims['right'],
      fill=self.color
    )
    canvas.create_text((self.pixel_dims['top'] + 21, self.pixel_dims['left'] + 12), text=self.id)
