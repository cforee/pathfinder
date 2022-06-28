import math

class Node:
  def __init__(self, node_x, node_y, size_in_px, config):
    self.id = '{}_{}'.format(node_x, node_y)
    self.x = node_x
    self.y = node_y
    self.size_in_px = size_in_px
    self.color = config['color']
    self.type = config['type']
    self.walkable = config['walkable']

    self.pixel_dims = {
      'top': self.y * self.size_in_px,
      'right': self.x * size_in_px + self.size_in_px,
      'bottom': self.y * size_in_px + self.size_in_px,
      'left': self.x * self.size_in_px
    }

  def draw(self, canvas):
    canvas.create_rectangle(
      self.pixel_dims['top'],
      self.pixel_dims['left'],
      self.pixel_dims['bottom'],
      self.pixel_dims['right'],
      fill=self.color
    )
    canvas.create_text((self.pixel_dims['top'] + 21 ,self.pixel_dims['left'] + 12), text=self.id)
